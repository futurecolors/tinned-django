# coding: utf-8


class EmailBaseSettings(object):
    # Assume we have local smpt
    EMAIL_HOST = 'localhost'
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST_USER = ''
    EMAIL_PORT = 587
    EMAIL_USE_TLS = False

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # Make emails async via celery
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'


class EmailDebugSettings(object):
    EMAIL_DEBUG = True  # All email goes to debug address instead of real recipients
    EMAIL_DEBUG_ADDRESSES = ('mail@example.com', )
    CELERY_EMAIL_BACKEND = 'apps.cms.utils.email.DebugSMTPEmailBackend'
