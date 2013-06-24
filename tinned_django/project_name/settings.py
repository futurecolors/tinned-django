# coding: utf-8
""" Class-based settings for different configurations
"""
import os
from configurations import Settings
from .config import DjangoSettings, AppsSettings
from .config import CompressEnabled


class BaseSettings(DjangoSettings, AppsSettings, Settings):
    DEBUG = False

    ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    PROJECT_ROOT = os.path.join(ROOT_PATH, '{{ project_name }}')
    PROJECT_NAME = '{{ project_name }}'
    ROOT_URLCONF = '{{ project_name }}.urls'
    SECRET_KEY = '{{ secret_key }}'
    SITE_ID = 1
    ANONYMOUS_USER_ID = 1  # Guardian
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    @property
    def INSTALLED_APPS(self):
        apps = (
            # Project apps 'apps.*'
            # ...

            # 3rd-party apps
            'south',
            'sorl.thumbnail',
            'pytils',
            'pymorphy',
            'admin_tools',
            'admin_tools.theming',
            'admin_tools.menu',
            'admin_tools.dashboard',
            'compressor',
            'django_nose',
            'mptt',
            'widget_tweaks',
            'guardian',
            'djcelery',
            'ckeditor',
            'waffle',

            # Django
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.staticfiles',
            'django.contrib.messages',
            'django.contrib.comments',
            'django.contrib.sites',
        )

        if self.DEBUG_TOOLBAR_ENABLED:
            apps += ('debug_toolbar',)
        return apps


class Development(BaseSettings):
    DEBUG = True
    DEBUG_TOOLBAR_ENABLED = True
    TEMPLATE_DEBUG = True


class Testing(BaseSettings):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'testing.db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
    NOSE_ARGS = ['--nocapture', '--nologcapture', '--with-id']
    SOUTH_TESTS_MIGRATE = False
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )


class Staging(CompressEnabled, BaseSettings):
    """ Change settings for db, cache etc."""
    DEBUG = False


class Production(CompressEnabled, BaseSettings):
    """ Change settings for db, cache etc."""
    DEBUG = False
