import os
from .settings import *
from .settings import BASE_DIR

# Use WEBSITE_HOSTNAME if available, otherwise fallback to localhost


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
ALLOWED_HOSTS = ['tribhuj-esm.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://tribhuj-esm.azurewebsites.net']

DEBUG = False

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#python manage.py dbshell
# if connection_string:
#     parameters = dict(pair.split('=') for pair in connection_string.split())
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': parameters['dbname'],
#             'HOST': parameters['host'],
#             'USER': parameters['user'],
#             'PASSWORD': parameters['password'],
#         }
#     }
# else:
#     DATABASES = {}
# ---------------- DATABASE (POSTGRESQL) ----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}