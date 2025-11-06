import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'

    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME', 'admin_panel')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_HTTPONLY = True

    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True

    @classmethod
    def init_app(cls, app):
        if not os.environ.get('SECRET_KEY'):
            raise ValueError("SECRET_KEY must be set in production environment")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}