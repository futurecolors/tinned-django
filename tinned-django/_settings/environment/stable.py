# -*- coding: utf-8 -*-

DEBUG = False

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

# Включаем компрессию по-умолчанию
COMPRESS = True
COMPRESS_OFFLINE = True