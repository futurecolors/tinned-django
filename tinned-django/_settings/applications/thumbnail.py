# -*- coding: utf-8 -*-

# Настройки модуля миниатюр
THUMBNAIL_PREFIX = 'thumbs/'
THUMBNAIL_DEBUG = False
THUMBNAIL_DUMMY = False
THUMBNAIL_UPSCALE = False

#  This engine uses the ImageMagick convert or GraphicsMagic gm convert command. Features:
#  Easy to install
#  Produces high quality images
#  It is pretty fast
#  Can handle CMYK sources
#  It is a command line command, that is less than ideal.
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'

# Хранилище для thumbnail
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_DB = 1