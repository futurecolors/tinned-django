# -*- coding: utf-8 -*-
import os
from settings import ROOT_PATH

# Медиа (пользовательский upload)
MEDIA_ROOT = os.path.join(ROOT_PATH, '_media')
MEDIA_URL = '/_media/'
ADMIN_MEDIA_PREFIX = '/_static/admin/'

# Статика
STATIC_ROOT = os.path.join(ROOT_PATH, '_static')
STATIC_URL = '/_static/'
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)