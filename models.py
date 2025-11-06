from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    credentials = db.relationship('Credential', backref='user', lazy=True, cascade='all, delete-orphan')

    def get_id(self):
        return str(self.uid)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return f'<User {self.email}>'


class Credential(db.Model):
    __tablename__ = 'credentials'

    cred_id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid', ondelete='CASCADE'), nullable=False)
    email = db.Column(db.String(120), nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Credential {self.email}>'