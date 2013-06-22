# coding: utf-8


class SessionSettings(object):
    SESSION_ENGINE = 'django.contrib.sessions.backends.file'
    SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 4

    def SESSION_COOKIE_NAME(self):
        return self.PROJECT_NAME

    LOGIN_URL = '/admin/'
    MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'