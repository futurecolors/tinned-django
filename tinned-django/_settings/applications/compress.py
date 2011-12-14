# -*- coding: utf-8 -*-
from _settings.applications.redactor import REDACTOR_SETTINGS
from _settings.media import MEDIA_URL, STATIC_URL
from redactor import REDACTOR_ELEMENTS


COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']
