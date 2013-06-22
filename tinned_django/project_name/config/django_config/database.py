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