# -*- coding: utf-8 -*-

DEBUG = False

DATABASES = {
    'default': {
        'NAME': '{{ DB_NAME }}_staging',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '{{ DB_USER }}',
        'PASSWORD': '{{ DB_PASSWORD }}',
        'HOST': 'localhost',
        'OPTIONS': {"init_command": "SET storage_engine=INNODB"}
    }
}

# Redis
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'TIMEOUT': 60,
        'MAX_ENTRIES': 10000,
        'OPTIONS': {
            'DB': 2,
        },
    },
}

# Compress by default
COMPRESS = True
COMPRESS_OFFLINE = True