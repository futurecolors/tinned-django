# -*- coding: utf-8 -*-
from settings import (DEBUG, PROFILER_ENABLED, FIRELOGGER, DEBUG_TOOLBAR_ENABLED,
                      SENTRY_ENABLED, SWFUPLOAD_MIDDLEWARE_VIEWS)

MIDDLEWARE_CLASSES = (
    'fc.maintenance.middlewares.MaintenanceMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'annoying.middlewares.RedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

if SWFUPLOAD_MIDDLEWARE_VIEWS:
    MIDDLEWARE_CLASSES += ('fc.swfupload.middlewares.SWFUploadMiddleware',)

if DEBUG and PROFILER_ENABLED:
    MIDDLEWARE_CLASSES += ('fc.profile.middlewares.ProfileMiddleware',)

if DEBUG and FIRELOGGER:
    MIDDLEWARE_CLASSES += ('fc.profile.middlewares.FcFirePythonDjango',)

if DEBUG and DEBUG_TOOLBAR_ENABLED:
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
    LANGUAGE_CODE = 'en-us'

if SENTRY_ENABLED:
    MIDDLEWARE_CLASSES += ('sentry.client.middleware.Sentry404CatchMiddleware',)