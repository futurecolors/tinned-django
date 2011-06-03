# -*- coding: utf-8 -*-

DEBUG = False

DATABASES = {
    'default': {
        'NAME': '',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '',
        'PASSWORD': '',
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
            'DB': 1,
        },
    },
}

# Включаем компрессию по-умолчанию
COMPRESS = True
COMPRESS_OFFLINE = True