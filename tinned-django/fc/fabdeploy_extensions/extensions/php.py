# -*- coding: utf-8 -*-
from fab_deploy import utils
from fab_deploy.system import aptitude_install


@utils.run_as_sudo
def php_cli_install():
    ''' Installs php5 CLI'''
    aptitude_install('php5-cli')


@utils.run_as_sudo
def php_gd_install():
    ''' Installs gd for php5'''
    aptitude_install('php5-gd')