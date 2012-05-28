# -*- coding: utf-8 -*-
import logging.config
import os

# Настройка панели дебага
DEBUG_TOOLBAR_ENABLED = False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda x: True,
    'HIDE_DJANGO_SQL': False,
}

# Включение профайлинга
PROFILER_ENABLED = False

# Настройки Sentry
SENTRY_ENABLED = True

# Настройки логирования
PATH = os.path.abspath(os.path.dirname(__file__))
logging.config.fileConfig(PATH + '/logging.ini')