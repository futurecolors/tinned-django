# coding: utf-8
import os


class MediaSettings(object):

    @property
    def MEDIA_ROOT(self):
        return os.path.join(self.PROJECT_ROOT, 'media')

    @property
    def STATIC_ROOT(self):
        return os.path.join(self.PROJECT_ROOT, 'static')

    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = ()

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    )
