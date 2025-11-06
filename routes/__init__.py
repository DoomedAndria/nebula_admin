"""
Routes package for Nebula Admin
"""
from .main import main_bp
from .auth import auth_bp
from .errors import errors_bp

__all__ = ['main_bp', 'auth_bp', 'errors_bp']