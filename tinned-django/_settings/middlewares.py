# -*- coding: utf-8 -*-
from _settings import DEBUG, DEBUG_TOOLBAR_ENABLED, SENTRY_ENABLED


MIDDLEWARE_CLASSES = (
    #    'fc.maintenance.middlewares.MaintenanceMiddleware',
    'annoying.middlewares.RedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

if DEBUG and DEBUG_TOOLBAR_ENABLED:
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
    LANGUAGE_CODE = 'en-us'

if SENTRY_ENABLED:
    MIDDLEWARE_CLASSES += ('sentry.client.middleware.Sentry404CatchMiddleware',)