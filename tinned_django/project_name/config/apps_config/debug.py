# coding: utf-8


class DebugSettings(object):
    DEBUG_TOOLBAR_ENABLED = False

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': lambda x: True,
        'HIDE_DJANGO_SQL': False,
    }

    # Empty for no logging
    # Don't use with SENTRY_DSN together, this will take prescendence
    # http://raven.readthedocs.org/en/latest/config/django.html
    RAVEN_CONFIG = {
        'dsn': '',  # http://public:secret@example.com/1
    }
