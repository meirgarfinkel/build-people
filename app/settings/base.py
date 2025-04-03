import os
from pathlib import Path
from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Security
SITE_ID = 1

# Application definition
INSTALLED_APPS = [
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
    # Local
    'shared',
    'users',
    'gratify',
    'theme',
    'tailwind'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Manually managed static files
    BASE_DIR / "theme/static",  # Tailwind’s build output directory
]
STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Authentication
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/gratify/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/users/login'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

# Tailwind
TAILWIND_APP_NAME = 'theme'

# Email
DEFAULT_FROM_EMAIL = 'no-reply@buildpeople.com'

# Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Custom settings
MESSAGE_TAGS = {
    messages.DEBUG: "bg-gray-300",
    messages.INFO: "bg-gray-300",
    messages.SUCCESS: "bg-green-500",
    messages.WARNING: "bg-yellow-500",
    messages.ERROR: "bg-red-500",
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
