"""
Django settings for shakecardsweb project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ['DJANGO_SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if environ['DEBUG'] == 'True' else False

ALLOWED_HOSTS = [environ['HOST'], ]

CSRF_TRUSTED_ORIGINS = [environ['CSRF_ORIGINS'], ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qr_code',
    'debug_toolbar',
    'colorfield',
    'base',
    'company',
    'contact',
    'service',
    'tool',
    'user',
    'web',
    'colorTemplate'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'shakecardsweb.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'shakecardsweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ['DATABASE_NAME'],
        'USER': environ['DATABASE_USER'],
        'PASSWORD': environ['DATABASE_PASSWORD'],
        'HOST': environ['DATABASE_HOST'],
        'PORT': environ['DATABASE_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

if DEBUG:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR /'staticfiles'
    ]
    MEDIA_ROOT= BASE_DIR / 'media'
else:
    STATIC_URL = 'https://%s/%s/' %(environ['AWS_BUCKET_URL'], environ['AWS_FOLDER'])
    STATICFILES_STORAGE = 'aws_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'aws_storages.PublicMediaStorage'

    AWS_STORAGE_BUCKET_NAME = environ['AWS_BUCKET_NAME']
    AWS_FOLDER = environ['AWS_FOLDER']
    AWS_ACCESS_KEY_ID = environ['AWS_S3_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = environ['AWS_S3_SECRET_KEY']
    STATICFILES_DIRS = [
        BASE_DIR /'staticfiles'
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = type(str('c'), (), {'__contains__': lambda *a: True})()

