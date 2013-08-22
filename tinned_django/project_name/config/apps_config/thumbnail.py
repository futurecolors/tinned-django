# coding: utf-8


class ThumbnailSettings(object):
    """ sorl-thumbnail """
    THUMBNAIL_PREFIX = 'thumbs/'
    THUMBNAIL_DEBUG = False
    THUMBNAIL_DUMMY = False
    THUMBNAIL_UPSCALE = False

    #  This engine uses the ImageMagick convert or GraphicsMagic
    #  gm convert command.
    #
    #  Features:
    #    * Easy to install
    #    * Produces high quality images
    #    * It is pretty fast
    #    * Can handle CMYK sources
    #  It is a command line command, that is less than ideal.
    THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
    # non-linear for ImageMagick, otherwise gamma will be screwed
    THUMBNAIL_COLORSPACE = 'sRGB'

    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
    THUMBNAIL_REDIS_UNIX_SOCKET_PATH = '/var/run/redis/{{ project_name}}.sock'
    THUMBNAIL_REDIS_DB = 1


class ThumbnailDebug(ThumbnailSettings):
    """ For local development"""
    THUMBNAIL_DUMMY = True
    THUMBNAIL_DUMMY_SOURCE = 'http://lorempixel.com/%(width)s/%(height)s/nature'
