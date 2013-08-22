# coding: utf-8


class CacheDummySettings(object):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


class CacheRedis(object):
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '/var/run/redis/{{ project_name}}.sock',
            'TIMEOUT': 60,
            'MAX_ENTRIES': 10000,
            'OPTIONS': {
                'DB': 1,
            },
        },
    }
