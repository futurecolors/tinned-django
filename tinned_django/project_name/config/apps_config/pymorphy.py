# coding: utf-8
import os


class PyMorphy(object):
    @property
    def PYMORPHY_DICTS(self):
        return {
            'ru': {
                'dir': os.path.join(self.ROOT_PATH, 'data/pymorphy'),
            },
        }