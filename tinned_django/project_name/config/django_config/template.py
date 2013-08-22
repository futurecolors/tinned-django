# coding: utf-8
import os


class TemplateSettings(object):

    @property
    def TEMPLATE_CONTEXT_PROCESSORS(self):
        processors = (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'django.core.context_processors.request',
            'django.contrib.messages.context_processors.messages',
        )
        if self.DEBUG:
            processors += ('django.core.context_processors.debug',)
        return processors

    TEMPLATE_LOADERS = (
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader',
    )

    def TEMPLATE_DEBUG(self):
        return self.DEBUG

    def TEMPLATE_DIRS(self):
        return (
            os.path.join(self.PROJECT_ROOT, 'templates'),
        )


class CachedTemplates(TemplateSettings):
    """ Speeds up rendering if template tags are thread-safe.
        They should be, so we're using it.
    """
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.filesystem.Loader',
        )),
    )
