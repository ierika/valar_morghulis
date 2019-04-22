import pymysql

from .base import *


DEBUG = True

# Django Debug Toolbar - Enable in local env.
INTERNAL_IPS = ALLOWED_HOSTS

# Database
DB_ENGINE = get_env('DB_ENGINE')

if DB_ENGINE == 'django.db.backends.mysql':
    pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': get_env('DB_HOST'),
        'USER': get_env('DB_USER'),
        'PASSWORD': get_env('DB_PASSWORD'),
        'NAME': get_env('DB_NAME'),
    }
}
