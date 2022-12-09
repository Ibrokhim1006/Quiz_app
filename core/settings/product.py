from .base import *

ALLOWED_HOSTS = ['*']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiz_app',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}