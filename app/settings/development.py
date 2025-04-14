import os
import socket
from pathlib import Path
from dotenv import load_dotenv
from django.contrib import messages

# ─────────────────────────────
# Base Setup
# ─────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env.dev')

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = ['127.0.0.1'] + [ip.rsplit('.', 1)[0] + '.1' for ip in ips]

SITE_ID = 1

# ─────────────────────────────
# Installed Apps
# ─────────────────────────────
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party
    'crispy_forms',
    'crispy_tailwind',
    'hx_requests',
    # 'debug_toolbar',
    # 'django_extensions',

    # Local apps
    'shared',
    'users',
    'build_people',
    'theme',
    'tailwind',
]

# ─────────────────────────────
# Middleware
# ─────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# ─────────────────────────────
# URLs and WSGI
# ─────────────────────────────
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

# ─────────────────────────────
# Templates
# ─────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ─────────────────────────────
# Database
# ─────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        'CONN_MAX_AGE': 0,
    }
}

# ─────────────────────────────
# Authentication
# ─────────────────────────────
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/login'

# ─────────────────────────────
# Static Files
# ─────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / "theme/static",
]
STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# ─────────────────────────────
# Email
# ─────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "no-reply@localhost"

# ─────────────────────────────
# Internationalization
# ─────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ─────────────────────────────
# Password Validators
# ─────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─────────────────────────────
# Crispy Forms
# ─────────────────────────────
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'
CRISPY_FAIL_SILENTLY = False

# ─────────────────────────────
# Tailwind
# ─────────────────────────────
TAILWIND_APP_NAME = 'theme'

# ─────────────────────────────
# Debug Toolbar
# ─────────────────────────────
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

# ─────────────────────────────
# Security
# ─────────────────────────────
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://0.0.0.0:8000',
]
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = "SAMEORIGIN"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# ─────────────────────────────
# Custom
# ─────────────────────────────
MESSAGE_TAGS = {
    messages.DEBUG: "bg-gray-300",
    messages.INFO: "bg-gray-300",
    messages.SUCCESS: "bg-green-500",
    messages.WARNING: "bg-yellow-500",
    messages.ERROR: "bg-red-500",
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
