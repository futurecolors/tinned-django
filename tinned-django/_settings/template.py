# -*- coding: utf-8 -*-
import os
from settings import ROOT_PATH, DEBUG

# Настройки шаблонов
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)
if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)