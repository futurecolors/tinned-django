# -*- coding: utf-8 -*-
from _settings import *

STATIC_ROOT = ROOT_PATH + '/static'

INSTALLED_APPS = (
    # Приложения проекта 'apps.*'


    # Приложения сторонних разработчиков
    'south',
    'sorl.thumbnail',
    'pytils',
    'pymorphy',
    'indexer',
    'paging',
    'sentry',
    'sentry.client',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'compressor',
    'django_any',
    'django_jenkins',
    'mptt',
    'widget_tweaks',
    'djangosphinx',
    'guardian',
    'djcelery',

    # Чужие приложения, которые хорошо бы форкнуть

    # Наши приложения
    'fc.maintenance',
    'fc.weightmixin',

    # Приложения Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    )

# djCelery
import djcelery
djcelery.setup_loader()

# Для django-jenkins
PROJECT_APPS = [app for app in INSTALLED_APPS if app.startswith('apps.')]


# local settings
try:
    from _settings.environment.local import *
except ImportError:
    pass

test_selenium_flags = ['test_selenium']
IS_SELENIUM = bool(filter(lambda x: x in sys.argv, test_selenium_flags))

if IS_SELENIUM:
    try:
        from _settings.environment.selenium import *
    except ImportError:
        pass

# hack for jenkins selenium
if 'jenkins' in sys.argv and 'selenium_tests' in sys.argv:
    TEST_RUNNER = 'selenium_tests.runners.JenkinsTestRunner'
