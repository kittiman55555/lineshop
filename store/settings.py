"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
#import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#mefia folder setting
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_w(ctp$ndu2)spbwp&%o+)z$o+m3s8ct*(r5nq+!pq^8*9qw$k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'lineshops.herokuapp.com']
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', '.herokuapp.com', '.ngrok.io']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_swagger',
    'rest_framework','customer','product','categories','orders',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
]



ROOT_URLCONF = 'store.urls'

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

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'storelines.sqlite3'),
#     }
# }

# DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd29ofjerekadm5',
#         'USER': 'syfkitdsfpcuss',
#         'PASSWORD': '88f73b2c90009144f0e906d1cad1e48c52237a57196bf217f0ba545861554446',
#         'HOST': 'ec2-50-16-197-244.compute-1.amazonaws.com',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'd29ofjerekadm5'),
        'USER': os.environ.get('DB_USER', 'syfkitdsfpcuss'),
        'PASSWORD': os.environ.get('DB_PASS', '88f73b2c90009144f0e906d1cad1e48c52237a57196bf217f0ba545861554446'),
        'HOST': 'ec2-50-16-197-244.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}



import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'd3vrpusptlmsbg',
#     'USER': 'ehvaonciwgxotl',
#     'PASSWORD': '21071b43ee312a908e74ece41a19d6564969ed4d27832c23185d1b8c3cb31867',
#     'HOST': 'ec2-174-129-227-51.compute-1.amazonaws.com',
#     'PORT': '5432'
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#del DATABASES['default']['OPTIONS']['sslmode']