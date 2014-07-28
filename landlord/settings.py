import os

import django.conf.global_settings as DEFAULT_SETTINGS


# Repository directory
ROOT = os.path.dirname(os.path.dirname(__file__))


# path bases things off of ROOT
def path(*a):
    return os.path.abspath(os.path.join(ROOT, *a))

# settings for translation
_ = lambda s: s
LANGUAGES = (
    ('zh-cn', _('China')),
)


LOGIN_URL = '/account/signin/'
ALLOWED_HOSTS = []
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-CN'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''


STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (

)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'landlord.urls'

WSGI_APPLICATION = 'landlord.wsgi.application'

TEMPLATE_DIRS = (
    path('landlord', 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'landlord.account',
    'landlord.common',
    'landlord.stu_act',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


try:
    from landlord.config.production import *
except ImportError:
    from landlord.config.development import *
