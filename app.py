import os
import pymysql
from flask import Flask
from flask_login import LoginManager
from models import db, User
from config import config

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'


def ensure_database_exists(config_obj):
    """Create database if it doesn't exist"""
    try:
        # Connect to MySQL without specifying database
        connection = pymysql.connect(
            host=config_obj.DB_HOST,
            user=config_obj.DB_USER,
            password=config_obj.DB_PASSWORD
        )
        cursor = connection.cursor()

        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config_obj.DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print(f"✓ Database '{config_obj.DB_NAME}' is ready")

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Warning: Could not ensure database exists: {e}")
        print("Please create the database manually if the app fails to start")


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])

    # Ensure database exists before connecting
    ensure_database_exists(config[config_name])

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from routes import main_bp, auth_bp, errors_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login"""
    return User.query.get(int(user_id))


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)