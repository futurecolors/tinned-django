# -*- coding: utf-8 -*-
import os
from _settings import ROOT_PATH

# Медиа (пользовательский upload)
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Статика
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)