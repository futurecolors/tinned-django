# coding: utf-8
from .settings import Development


class userSettings(Development):
    """ Put your local settings here, so that they won't affect other developers

        To activate this settings, set these variables in your env:

        export DJANGO_SETTINGS_MODULE={{ project_name }}.live_settings
        export DJANGO_CONFIGURATION=<user>Settings

        Add them in your virtualenv init script env/bin/activate,
        not your global environment
    """
