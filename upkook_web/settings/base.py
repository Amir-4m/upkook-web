#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import os


def get_env_var(key, default=None):
    return os.environ.get('UPKOOK_WEB_%s' % key, default)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'upkook-web.sqlite3',
    }
}

# Django settings for upkook web project.

# The top directory for this project. Contains requirements/, manage.py,
# and README.rst, a upkook directory with settings etc (see
# PROJECT_PATH), as well as a directory for each Django app added to this
# project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# The directory with this project's templates, settings, urls, static dir,
# wsgi.py, fixtures, etc.
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'upkook_web')

DEBUG = get_env_var('DEBUG', 'False') == 'True'

TEST = get_env_var('TEST', 'False') == 'True'

ADMINS = (
    ('Saeed Salehian', 'saeed@upkook.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS', "127.0.0.1,localhost").split(",")

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_env_var('SECRET_KEY', 'fake-key')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = get_env_var('TIME_ZONE', 'Asia/Tehran')

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = get_env_var('LANGUAGE_CODE', 'en-us')

SITE_ID = 1

SITE_URL = get_env_var('SITE_URL', 'http://127.0.0.1/')

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/public/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = get_env_var('MEDIA_URL', '/media/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/public/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# Path to generated static files from JavaScript catalog
STATICI18N_ROOT = os.path.join(PROJECT_PATH, 'static', )

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = get_env_var('STATIC_URL', '/static/')

# Additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
        'DIRS': (
            os.path.join(PROJECT_PATH, 'templates'),
        ),
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': (
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
            ),
            # List of callables that know how to import templates from
            # various sources.
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )
        }
    }
]

# List of compiled regular expression objects representing User-Agent strings
# that are not allowed to visit any page, system-wide.
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-DISALLOWED_USER_AGENTS
DISALLOWED_USER_AGENTS = []

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-APPEND_SLASH
APPEND_SLASH = False

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-PREPEND_WWW
PREPEND_WWW = False

# A boolean that specifies whether to output the ETag header.
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-USE_ETAGS
USE_ETAGS = True

MIDDLEWARE_CLASSES = (
    # Adds a few conveniences for perfectionists (i.e. URL rewriting)
    'django.middleware.common.CommonMiddleware',
)

if DEBUG or TEST:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
else:  # pragma: no cover
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

LOGIN_URL = get_env_var('LOGIN_URL', '/login')

ROOT_URLCONF = 'upkook_web.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'upkook_web.wsgi.application'

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(PROJECT_PATH, 'logs', 'upkook.log'),
            'maxBytes': 20 * 1024 * 1024,  # 20 MBs
            'backupCount': 40,
        },
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'] if DEBUG else ['file'],
            'propagate': True,
            'level': 'WARNING' if DEBUG else 'ERROR',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING' if DEBUG else 'ERROR',
            'propagate': True,
        },
        'upkook': {
            'handlers': ['console'] if DEBUG else ['sentry', 'file'],
            'level': 'DEBUG' if DEBUG else 'ERROR',
            'propagate': True,
        },
        'raven': {
            'level': 'WARNING' if DEBUG else 'ERROR',
            'handlers': ['console'] if DEBUG else ['file'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'WARNING' if DEBUG else 'ERROR',
            'handlers': ['console'] if DEBUG else ['file'],
            'propagate': False,
        },
    }
}

INSTALLED_APPS = (
    # Internal Django Apps
    'django.contrib.staticfiles',

    # External Apps
    # Sentry
    'raven.contrib.django.raven_compat',

    # Project Apps

    # cookie and session domain name. must be string
)

SESSION_COOKIE_DOMAIN = get_env_var('SESSION_COOKIE_DOMAIN')

CSRF_COOKIE_DOMAIN = get_env_var('CSRF_COOKIE_DOMAIN')

RAVEN_CONFIG = {
    'dsn': get_env_var('SENTRY_DSN'),
}
