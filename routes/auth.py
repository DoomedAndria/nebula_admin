from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import db, User, Credential

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # TODO: Implement login logic with Flask-WTF forms
        # email = request.form.get('email')
        # password = request.form.get('password')
        # remember = request.form.get('remember', False)

        # Placeholder for form handling
        flash('Login functionality will be implemented with Flask-WTF forms', 'info')
        pass

    return render_template('login.jinja2')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # TODO: Implement registration logic with Flask-WTF forms
        # firstname = request.form.get('firstname')
        # lastname = request.form.get('lastname')
        # email = request.form.get('email')
        # password = request.form.get('password')

        # Placeholder for form handling
        flash('Registration functionality will be implemented with Flask-WTF forms', 'info')
        pass

    return render_template('register.jinja2')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))