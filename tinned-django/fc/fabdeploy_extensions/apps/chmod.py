# -*- coding: utf-8 -*-
from fabric.api import run, env, settings
from fab_deploy import utils

@utils.run_as('root')
def set_chmod():
    """ Setups chmods """
    dirs = ('_media', '_media/upload', '_static/compressed', '_data')

    with cd(env.conf['PROJECT_DIR']):
        for dir in dirs:
            run('chmod 777 -R {0}'.format(dir))
  