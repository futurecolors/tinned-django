# -*- coding: utf-8 -*-
import os

# Включаем дебаг
DEBUG = True
FIRELOGGER = True

# Базы данных
DATABASES = {
    'default': {
        'NAME': '',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'OPTIONS': {"init_command": "SET storage_engine=INNODB"}
    }
}

# Выключаем кеш и храним сессии в базе (иначе не сможем авторизоваться)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Подключаем настройки для пользователей
try:
    execfile('{0}/_settings/environment/users/{1}.py'.format(ROOT_PATH, os.environ.get('USER')))
except Exception:
    pass

# Не надо добавлять сюда настройки, т.к. их нельзя будет переопределить в юзерконфигах
# Добавляйте новые настройки перед execfile