# -*- coding: utf-8 -*-
import os, sys

# Root-директория
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_PATH)

# Кодовое название проекта
PROJECT_NAME = '{{ PROJECT_NAME }}'

# Название сайта
SITE_NAME = '{{ PROJECT_NAME }}'

# окружение (development либо production)
DJANGO_SETTINGS_ENVIRONMENT = os.environ.get('DJANGO_SETTINGS_ENVIRONMENT') or 'development'

# Устанавливаем значение DEBUG
if DJANGO_SETTINGS_ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

# Время и языки
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
USE_L10N = True

# Для Sites framework
SITE_ID = 1

# Урлы
ROOT_URLCONF = 'urls'

# Секретный ключ
SECRET_KEY = '{{ SECRET_KEY }}'


# Системные настройки
from _settings.media import *
from _settings.template import *
from _settings.session import *
from _settings.cache import *
from _settings.email import *


# Настройки приложений
from _settings.applications import *


# Настройки для окружений
execfile('{0}/_settings/environment/{1}.py'.format(ROOT_PATH, DJANGO_SETTINGS_ENVIRONMENT))


# Подключение настроек
from _settings.middlewares import *
from _settings.installed_apps import *