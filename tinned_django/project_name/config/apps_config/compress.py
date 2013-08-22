# coding: utf-8


less_command = 'lessc {infile} {outfile}'


class CompressSettings(object):
    COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                            'compressor.filters.cssmin.CSSMinFilter']
    COMPRESS_PRECOMPILERS = (
        ('text/less', less_command + ' --rootpath=../'),
    )
    COMPRESS_CSS_HASHING_METHOD = 'content'


class CompressEnabled(CompressSettings):
    COMPRESS_ENABLED = True
    COMPRESS_OFFLINE = True

    COMPRESS_PRECOMPILERS = (
        ('text/less', less_command),
    )
