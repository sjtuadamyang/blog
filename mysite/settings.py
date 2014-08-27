"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yyi0u+61@57@qa3z@r3*^ykqnc!v(l&8z+9c1598*l!teu25+d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party apps 
    'easy_thumbnails',
    'south',
    'storages',

    # my apps
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config(default='postgres://yangzhenxi:@localhost:5432/yangzhenxi')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Media asset configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL needs to be the same as the MEDIA_ROOT prefix so that in DEBUG mode, the media url can be served.
MEDIA_URL = '/media/'

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

# Static asset configuration using S3 in production
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = 'adamyang_personal_blog'
    AWS_QUERYSTRING_AUTH = False  # Don't include auth in every url. This will fix the admin image url sandwish issue.
    STATICFILES_STORAGE = 's3utils.StaticRootS3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL + '/static/'
    DEFAULT_FILE_STORAGE = 's3utils.MediaRootS3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = 's3utils.MediaRootS3BotoStorage'
    MEDIA_URL = S3_URL + '/media/'
    AWS_ACCESS_KEY_ID = 'AKIAI75UNDXXRHB6FGOA'
    AWS_SECRET_ACCESS_KEY = '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'


# Easy-thumbnail configuration
THUMBNAIL_DEBUG = True
THUMBNAIL_ALIASES = {
    'blog.Post': {
        'standard': {
            'size': (290, 212),
            'crop': True,
        }
    }
}

