# coding: utf-8
import os


class DatabaseSettings(object):
    DATABASES = {
        'default': {
            'NAME': '{{ project_name }}_{0}'.format(os.environ.get('USER')),
            'ENGINE': 'django.db.backends.mysql',
            'USER': '{{ project_name }}',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {'init_command': 'SET storage_engine=INNODB'}
        }
    }


class DevDatabaseSettings(object):
    DATABASES = {
        'default': {
            'NAME': '{{ project_name }}_dev',
            'ENGINE': 'django.db.backends.mysql',
            'USER': '{{ project_name }}_dev',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {'init_command': 'SET storage_engine=INNODB'}
        }
    }


class RcDatabaseSettings(object):
    DATABASES = {
        'default': {
            'NAME': '{{ project_name }}_rc',
            'ENGINE': 'django.db.backends.mysql',
            'USER': '{{ project_name }}_rc',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {'init_command': 'SET storage_engine=INNODB'}
        }
    }


class ProdDatabaseSettings(object):
    DATABASES = {
        'default': {
            'NAME': '{{ project_name }}',
            'ENGINE': 'django.db.backends.mysql',
            'USER': '{{ project_name }}',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {'init_command': 'SET storage_engine=INNODB'}
        }
    }
