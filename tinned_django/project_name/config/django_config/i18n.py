# coding: utf-8
import os


class LocaleSettings(object):
    TIME_ZONE = 'Europe/Moscow'
    LANGUAGE_CODE = 'ru'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    LANGUAGES = (
        ("ru", "Russian"),
        ("en", "English"),
    )

    def LOCALE_PATHS(self):
        return (
            os.path.join(self.ROOT_PATH, 'locale'),
        )

    PREFIX_DEFAULT_LOCALE = False