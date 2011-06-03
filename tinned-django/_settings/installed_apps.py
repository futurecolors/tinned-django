# -*- coding: utf-8 -*-
from settings import DEBUG, DEBUG_TOOLBAR_ENABLED

INSTALLED_APPS = (
    # Приложения проекта

    # Приложения сторонних разработчиков
    'south',
    'sorl.thumbnail',
    'pymorphy',
    'pytils',
    'indexer',
    'paging',
    'sentry',
    'sentry.client',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'compressor',
    #'ckeditor',

    # Наши приложения
    'fc.profile',
    'fc.maintenance',

    # Приложения Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
)

if DEBUG and DEBUG_TOOLBAR_ENABLED:
    INSTALLED_APPS += ('debug_toolbar',)