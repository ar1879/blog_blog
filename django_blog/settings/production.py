from .base import *


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2j87ttqq01e8a',
        'USER': 'whposopeyaynyu',
        'PASSWORD': 'be6ae783079626a932a18cea1201467ea92be0adeb78d76e60fbacd94820091a',
        'HOST': 'ec2-52-4-104-184.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogdev13.herokuapp.com']