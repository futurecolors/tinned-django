# coding: utf-8


class CacheSettings(object):

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            }
    }