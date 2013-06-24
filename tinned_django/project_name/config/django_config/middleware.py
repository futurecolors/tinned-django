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

        if self.RAVEN_MIDDLEWARES_ENABLED:
            middleware_classes.extend(['sentry.client.middleware.SentryResponseErrorIdMiddleware',
                                       'raven.contrib.django.middleware.Sentry404CatchMiddleware'])
        return tuple(middleware_classes)
