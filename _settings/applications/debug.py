# -*- coding: utf-8 -*-
from settings import ROOT_PATH
import logging.config

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

# Firelogger
FIRELOGGER = False

# Дебаг SQL в Firepython
FIREPYTHON_SQL = False

# Настройки логирования
logging.config.fileConfig(ROOT_PATH + '/_settings/applications/logging.ini')