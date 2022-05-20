"""
Django settings for instagram project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import json
from pathlib import Path
import os
import environ
import logging.config

# Intialize environment variables 
#env = environ.Env() 
environ.Env().read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', True)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')

# Base class for user Authentication 
AUTH_USER_MODEL = 'app.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'rest_framework', 
    'rest_framework.authtoken',
    'djoser', 
    'corsheaders',
    'drf_spectacular', 
    'storages',

    #
    'app', 
]

# DRF CONF 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication', 
    ), 
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ], 

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', 
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', 
    'PAGE_SIZE': 100, 
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}

# DJOSER conf 
DJOSER = {
    "USER_ID_FIELD": "username", 
    "LOGIN_FIELD":"email", 
    "SEND_ACTIVATION_EMAIL": False, 
    "ACTIVATION_URL": "activate/{uid}/{token}", 
    "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}", 
    "SERIALIZERS": {
        'token_create': None
    }
}

# Json WEB token AUTH (related to djoser.urls.jwt)
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
}

# OBJECT STORAGE CONFIGURATION 
AWS_ACCESS_KEY_ID = os.getenv('STATIC_ACCESS_KEY_ID', 'your_aws_key_id') 
AWS_SECRET_ACCESS_KEY = os.getenv('STATIC_SECRET_ACCESS_KEY', 'you_secret_access_key')
AWS_STORAGE_BUCKET_NAME = os.getenv('STATIC_BUCKET_NAME', 'you_static_bucket_name')
AWS_S3_ENDPOINT_URL = os.getenv('STATIC_ENDPOINT_URL', 'your_static_endpoint_url')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

AWS_CLOUDFRONT_KEY = os.environ.get('AWS_CLOUDFRONT_KEY', None).encode('ascii')
AWS_CLOUDFRONT_KEY_ID = os.environ.get('AWS_CLOUDFRONT_KEY_ID', None)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'pystagram/static'),
]


# This to upload our media to and S3 like storage bucket 
#DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "app.storage_backends.MediaStorage"

# storage backends config
if DEBUG == True: 
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else: 
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}'
    STATIC_ROOT = 'static/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'app.storage_backends.MediaStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'instagram.urls'

EMAIL_BACKEND = None 
SITE_NAME = "pystagram" 
DOMAIN = "localhost:3000" 
if not DEBUG: 
    PROTOCOL ="https" 
    DOMAIN = "api.pystagram.com"  

CORS_ALLOWED_ORIGINS = [
    "https://localhost:3000", 
    "http://localhost:3000", 
    "https://www.pystagram.com", 
    "http://www.pystagram.com",
]

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

WSGI_APPLICATION = 'instagram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'db.sqlite3', 
        'PASSWORD': '', 
        'USER': ''
    },

    'prod': {
        'ENGINE': 'django.db.backends.{}'.format(os.getenv('DATABASE_ENGINE', 'sqlite3')),
        'NAME': os.getenv('DATABASE_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DATABASE_USERNAME', 'pystagramuser'), 
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'password'), 
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'), 
        'PORT': os.getenv('DATABASE_PORT', 5432), 
        'OPTIONS': json.loads(
            os.getenv('DATABASE_OPTIONS', '{}')
        ),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True





# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Logging Configuration 
# Clear Prev Config 
LOGGING_CONFIG = None 

# Get loglevel from env 
LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper() 

logging.config.dictConfig({
    'version': 1, 
    'disable_existing_loggers': False, 
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(message)s',

        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler', 
            'formatter': 'console',
        },
    },
    'loggers':{
        '': {
            'level': LOGLEVEL, 
            'handlers': ['console', ],
        }
    }
})
