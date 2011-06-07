# -*- coding: utf-8 -*-
from fabric.api import run
from fab_deploy import utils

@utils.run_as_sudo
@utils.inside_project
def set_chmod():
    """ Setups chmods """
    dirs = ('_media', '_media/upload', '_static/compressed', '_data')

    for dir in dirs:
        run('chmod 777 -R {0}'.format(dir))
  