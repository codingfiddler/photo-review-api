"""
Django settings for sitereview project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6#s_mnuz&1)w9d_@%fbn=2yir-bvgb#gw6q(ba%yl9my1^!=@-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.photoreview.apps.PhotoReviewConfig',
    'rest_framework.authtoken',
    'boto3',
    'django_s3_storage',
    'django_filters',
    # 'storages',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'apps.wsgi.application'

AUTH_USER_MODEL = 'photoreview.CustomUser'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
db_host = os.environ.get('DB_HOST', 'postgres')
db_name = os.environ.get('DB_NAME', 'postgres')
db_user = os.environ.get('DB_USER', 'postgres')
db_password = os.environ.get('DB_PASSWORD', 'postgres')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': 5432,
    }
}

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = "photoreview.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# AWS_ACCESS_KEY_ID = 'AKIAQWCTCCDFBIEQGE56'
# AWS_SECRET_ACCESS_KEY = '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'

DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage' # storages.backends.s3boto3.S3Boto3Storage
# AWS_STORAGE_BUCKET_NAME = 'krino-photos'
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_BUCKET_NAME =  'krino-images'
AWS_S3_BUCKET_NAME_STATIC =  'krino-images'
STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage' #storages.backends.s3boto3.S3Boto3Storage
S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': 'uploads/',
        'allowed': ['image/jpg', 'image/jpeg', 'image/png'],
    },
}
AWS_S3_FILE_OVERWRITE = False
