"""
Django settings for my_project project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-((fkgft!04ps8*asyx1630yzqkj2e=9*_m%7*-(06s2v*l5n*^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.252.22', '0.0.0.0', '127.0.0.1', 'localhost']

CSRF_TRUSTED_ORIGINS = [
    'http://192.168.252.22',  # Internal IP
    'http://0.0.0.0',         # General wildcard
    'http://127.0.0.1',       # Localhost (IPv4)
    'http://localhost',       # Localhost (name)
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'channels',
# other apps
    'my_app',
]

ASGI_APPLICATION = 'my_project.asgi.application'

# WebSocket Backend
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

#Azure setup
AZURE_CLIENT_ID = '016456a3-8023-4c07-a345-3a89c8e3124d'
AZURE_CLIENT_SECRET = 'z2u8Q~XhEoytFzFP3OpPeJYRwjKQ7nGn.noTRcFi'
AZURE_TENANT_ID = '4a3f472f-6e15-42f9-8d9f-44654903975f'
AZURE_SCOPES = ['https://graph.microsoft.com/.default']
AZURE_EMAIL_ENDPOINT = 'https://graph.microsoft.com/v1.0/me/sendMail'

# Email setup for console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "my_project.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = "my_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Alwaysdata credentials for database usage
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'initmeeting_db',  # Database name from the image
        'USER': '379731_mabj',     # Database username
        'PASSWORD': 'MABJ1337',  # Replace with the actual password
        'HOST': 'mysql-initmeeting.alwaysdata.net',  # Database host
        'PORT': '3306',  # MySQL's default port
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Europe/Copenhagen'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Whitenoise for static files

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField" # Default primary key field type