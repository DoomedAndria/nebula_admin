from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse
from models import db, User, Credential

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember', False)

        if not email or not password:
            flash('Please provide both email and password.', 'danger')
            return render_template('login.jinja2')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Invalid email or password.', 'danger')
            return render_template('login.jinja2')

        if not user.is_active:
            flash('Your account has been deactivated. Please contact support.', 'warning')
            return render_template('login.jinja2')

        credential = Credential.query.filter_by(uid=user.uid).first()

        if not credential or not credential.check_password(password):
            flash('Invalid email or password.', 'danger')
            return render_template('login.jinja2')

        login_user(user, remember=bool(remember))
        flash(f'Welcome back, {user.firstname}!', 'success')

        next_page = request.args.get('next')
        if next_page and url_parse(next_page).netloc == '':
            return redirect(next_page)
        return redirect(url_for('main.index'))

    return render_template('login.jinja2')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        firstname = request.form.get('firstname', '').strip()
        lastname = request.form.get('lastname', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not all([firstname, lastname, email, password]):
            flash('All fields are required.', 'danger')
            return render_template('register.jinja2')

        if '@' not in email or '.' not in email:
            flash('Please provide a valid email address.', 'danger')
            return render_template('register.jinja2')

        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
            return render_template('register.jinja2')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('An account with this email already exists.', 'warning')
            return render_template('register.jinja2')

        try:
            user = User(
                firstname=firstname,
                lastname=lastname,
                email=email,
                is_active=True
            )
            db.session.add(user)
            db.session.flush()

            credential = Credential(
                uid=user.uid,
                email=email
            )
            credential.set_password(password)
            db.session.add(credential)

            db.session.commit()

            flash(f'Account created successfully! Welcome, {firstname}!', 'success')

            login_user(user)
            return redirect(url_for('main.index'))

        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'danger')
            print(f"Registration error: {e}")
            return render_template('register.jinja2')

    return render_template('register.jinja2')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))