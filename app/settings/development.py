from .base import *
import socket
from dotenv import load_dotenv


load_dotenv(BASE_DIR / '.env.dev')
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
INTERNAL_IPS = ['127.0.0.1', 'localhost']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        'CONN_MAX_AGE': 0,  # Disable persistent connections in dev
    }
}

# Debug Toolbar
INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "no-reply@localhost"

# Debugging
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1']
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,  # Always show toolbar
}
TEMPLATES[0]['OPTIONS']['debug'] = True

# Security
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://0.0.0.0:8000',
]
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = "SAMEORIGIN"

# Crispy forms
CRISPY_FAIL_SILENTLY = False
