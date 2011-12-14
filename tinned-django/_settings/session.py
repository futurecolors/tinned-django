# -*- coding: utf-8 -*-
from _settings import PROJECT_NAME

# Сессии
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 4 # куки должны жить месяц (как и сессия)
SESSION_COOKIE_NAME = PROJECT_NAME