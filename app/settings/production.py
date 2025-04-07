from .base import *
from app.utils.aws_secrets import get_parameter


# Environ
DB_NAME = get_parameter("/build-people/DB_NAME")
DB_USER = get_parameter("/build-people/DB_USER")
DB_PASSWORD = get_parameter("/build-people/DB_PASSWORD")
DB_HOST = get_parameter("/build-people/DB_HOST")
SECRET_KEY = get_parameter("/build-people/SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = [
    "localhost",
    "13.219.131.40",
    "buildpeople.com",
    "www.buildpeople.com",
]

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": "5432",
    }
}

# Security settings
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
