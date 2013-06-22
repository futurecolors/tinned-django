# coding: utf-8
import os


class CkeditorSettings(object):

    CKEDITOR_CONTENT_CSS = []
    BODY_CLASS = ''

    @property
    def CKEDITOR_MEDIA_PREFIX(self):
        return self.STATIC_URL + 'ckeditor/'

    @property
    def CKEDITOR_UPLOAD_PATH(self):
        return os.path.join(self.PROJECT_ROOT, 'media/upload')

    @property
    def CKEDITOR_CONFIGS(self):
        return {
            'default': {
                'height': 400,
                'width': 840,
                'language': 'ru',
                'uiColor': '#ebebeb',

                'toolbar': 'FC',
                'toolbar_FC': [
                    ['Cut', 'Copy', 'Paste'],
                    ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
                    ['Image'],
                    ['Bold', 'Italic', 'Underline', 'Strike'],
                    ['Styles', 'Templates'],
                    ['NumberedList', 'BulletedList'],
                    ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ['Link', 'Unlink', 'Anchor', 'SpecialChar'],
                    ['Source', 'Maximize'],
                    ['Print', 'Preview'],
                ],

                'bodyClass': self.BODY_CLASS,
                'contentsCss': [self.STATIC_URL + css_path for css_path in self.CKEDITOR_CONTENT_CSS],
                'customConfig': 'fc_config.js',
                'stylesSet': 'fc_styles',
                },

            'simple': {
                'height': 300,
                'width': 500,
                'language': 'ru',

                'removePlugins': 'scayt',
                'disableNativeSpellChecker': False,

                'toolbar': 'FC',
                'toolbar_FC': [
                    ['Undo', 'Redo', '-', 'RemoveFormat'],
                    ['Bold', 'Italic'],
                    ['NumberedList', 'BulletedList']
                ],

                'bodyClass': self.BODY_CLASS,
                'contentsCss': [self.STATIC_URL + css for css in self.CKEDITOR_CONTENT_CSS],
            }
    }


