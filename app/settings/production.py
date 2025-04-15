import os
import boto3
from pathlib import Path
from django.contrib import messages

# ─────────────────────────────
# Base Setup
# ─────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent

def get_parameter(name, with_decryption=True):
    client = boto3.client("ssm", region_name=os.environ.get("AWS_REGION", "us-east-1"))
    response = client.get_parameter(Name=name, WithDecryption=with_decryption)
    return response["Parameter"]["Value"]

# ─────────────────────────────
# Secrets & Env Vars
# ─────────────────────────────
SECRET_KEY = get_parameter("/build-people/SECRET_KEY")
DB_NAME = get_parameter("/build-people/DB_NAME")
DB_USER = get_parameter("/build-people/DB_USER")
DB_PASSWORD = get_parameter("/build-people/DB_PASSWORD")
DB_HOST = get_parameter("/build-people/DB_HOST")

DEBUG = False

ALLOWED_HOSTS = [
    "buildpeople.app",
    "www.buildpeople.app",
    "13.219.131.40",
]

SITE_ID = 1

# ─────────────────────────────
# Installed Apps
# ─────────────────────────────
INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Third-party
    "crispy_forms",
    "crispy_tailwind",
    "hx_requests",

    # Local apps
    "shared",
    "users",
    "build_people",
    "theme",
    "tailwind",
]

# ─────────────────────────────
# Middleware
# ─────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ─────────────────────────────
# URLs and WSGI
# ─────────────────────────────
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

# ─────────────────────────────
# Templates
# ─────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ─────────────────────────────
# Database
# ─────────────────────────────
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

# ─────────────────────────────
# Authentication
# ─────────────────────────────
AUTH_USER_MODEL = "users.User"
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/login"

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
# Internationalization
# ─────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ─────────────────────────────
# Static Files
# ─────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
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
DEFAULT_FROM_EMAIL = "no-reply@buildpeople.com"

# ─────────────────────────────
# Crispy Forms
# ─────────────────────────────
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# ─────────────────────────────
# Tailwind
# ─────────────────────────────
TAILWIND_APP_NAME = "theme"

# ─────────────────────────────
# Security
# ─────────────────────────────
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
USE_X_FORWARDED_HOST = True

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
