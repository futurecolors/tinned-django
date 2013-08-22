# coding: utf-8


class MiddlewareSettings(object):

    @property
    def MIDDLEWARE_CLASSES(self):
        middleware_classes = [
            'annoying.middlewares.RedirectMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'waffle.middleware.WaffleMiddleware',
        ]
        if self.DEBUG and self.DEBUG_TOOLBAR_ENABLED:
            middleware_classes.append('debug_toolbar.middleware.DebugToolbarMiddleware')

        # 404 Logging           http://raven.readthedocs.org/en/latest/config/django.html?highlight=sentry404catchmiddleware#logging
        # Message Reference     http://raven.readthedocs.org/en/latest/config/django.html?highlight=sentry404catchmiddleware#message-references
        if self.RAVEN_CONFIG.get('dsn'):
            middleware_classes.extend(['raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
                                       'raven.contrib.django.middleware.Sentry404CatchMiddleware'])
        return tuple(middleware_classes)
