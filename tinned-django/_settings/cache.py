# -*- coding: utf-8 -*-

# По-умолчанию выключаем кэш
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}