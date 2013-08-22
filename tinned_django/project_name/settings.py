# coding: utf-8
""" Class-based settings for different configurations
"""
import os
from configurations import Settings
from django.utils.importlib import import_module
from .config import DjangoSettings, AppsSettings, EmailDebugSettings, RcDatabaseSettings, DevDatabaseSettings, ProdDatabaseSettings
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
            'djcelery_email',
            'ckeditor',
            'waffle',
            'floppyforms',
            'django_extensions',
            'raven.contrib.django.raven_compat',

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

        if self.DEBUG and self.DEBUG_TOOLBAR_ENABLED:
            apps += ('debug_toolbar',)
        return apps


def get_local_settings():
    """ localSettings per developer

        For instance, for USER=prophet we will try to use
        mixin ``Prophet`` in CBS Live.
        If it is not present, no problem, exceptions is silenced.
    """
    try:
        developer_settings_name = os.environ.get('USER', '').title()
        live_settings = import_module('{{ project_name }}.live_settings')
        return getattr(live_settings, developer_settings_name)
    except (ImportError, AttributeError):
        class LocalSettings:
            pass
        return LocalSettings

LocalSettings = get_local_settings()


class BaseLive(EmailDebugSettings, BaseSettings):
    DEBUG = True
    DEBUG_TOOLBAR_ENABLED = True
    TEMPLATE_DEBUG = True


class Live(LocalSettings, BaseLive):
    pass


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


class Dev(DevDatabaseSettings, CompressEnabled, EmailDebugSettings, BaseSettings):
    """ Change settings for db, cache etc."""
    DEBUG = False


class Rc(RcDatabaseSettings, CompressEnabled, EmailDebugSettings, BaseSettings):
    """ Change settings for db, cache etc."""
    DEBUG = False


class Production(ProdDatabaseSettings, CompressEnabled, BaseSettings):
    """ Change settings for db, cache etc."""
    DEBUG = False
