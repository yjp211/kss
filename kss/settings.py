# -*- coding:utf-8 -*-
import os

DEBUG = True
DEBUG_LEVEL = 'DEBUG'
TEMPLATE_DEBUG = DEBUG

DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

PROJECT_NAME = 'kss'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '192.168.0.107:6379:0',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
            'SOCKET_TIMEOUT': 5,
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 10 * 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, STATIC_URL.strip("/")),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'ubp^wj6hhpgv-!$#&o7ne#9ua@0b6l(^*bte@8!c@3@4mnop#)'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'kss.urls'

WSGI_APPLICATION = 'kss.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


LOG_ROOT =  os.path.join(PROJECT_ROOT, 'log')
LOG_MAX_SIZE = 1024*1024*10 # 10 MB

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
            'location': {
                'format': '%(asctime)s %(module)10s::%(filename)-10s %(lineno)4d %(levelname)6s  - %(message)s'
            },
        },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'location'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'debug_handler': {
            'level': DEBUG_LEVEL,
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'debug.log'),
            'maxBytes': LOG_MAX_SIZE,
            'backupCount': 2,
            'formatter':'location',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'debug': {
            'handlers': ['debug_handler','console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }

}
