# coding: utf-8
from django_config import *
from apps_config import *


class DjangoSettings(DatabaseSettings, CacheDummySettings, LocaleSettings, LoggingSettings,
                     MediaSettings, MiddlewareSettings, SessionSettings, TemplateSettings):
    pass


class AppsSettings(AdminTools, CelerySettings, CkeditorSettings, CompressSettings,
                   DebugSettings, EmailBaseSettings, PyMorphy, ThumbnailSettings):
    pass
