# coding: utf-8


class CompressSettings(object):

    COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                            'compressor.filters.cssmin.CSSMinFilter']


class CompressEnabled(CompressSettings):
    COMPRESS_ENABLED = True
    COMPRESS_OFFLINE = True