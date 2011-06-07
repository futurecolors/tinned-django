# -*- coding: utf-8 -*-
from fab_deploy import utils
from fab_deploy.system import aptitude_install

__all__ = ['java_install']

@utils.run_as_sudo
def java_install():
    ''' Installs JRE '''
    aptitude_install('default-jre')