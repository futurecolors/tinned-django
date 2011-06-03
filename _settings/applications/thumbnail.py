# -*- coding: utf-8 -*-

# Настройки модуля миниатюр
THUMBNAIL_PREFIX = 'thumbs/'
THUMBNAIL_DEBUG = False
THUMBNAIL_DUMMY = False
THUMBNAIL_UPSCALE = False

# Хранилище для thumbnail
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_DB = 1