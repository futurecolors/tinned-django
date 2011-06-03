# -*- coding: utf-8 -*-
from fabric.api import run, env, settings
from fab_deploy import utils
from fab_deploy.system import aptitude_install

@run_as('root')
def install_java():
    aptitude_install('default-jre')