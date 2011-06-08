# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.contrib import files
from fab_deploy import utils
from fab_deploy import system


__all__ = ['uwsgi_install', 'uwsgi_setup', 'uwsgi_start', 'uwsgi_restart', 'uwsgi_reload']


@utils.run_as_sudo
def uwsgi_install():
    """ Installs uWSGI. """
    with cd(env.conf.SRC_DIR):
        with utils.virtualenv():
            sudo('pip install uwsgi')


@utils.run_as_sudo
def uwsgi_setup():
    """ Setups uWSGI. """
    sudo('adduser --system --no-create-home --disabled-login --disabled-password --group uwsgi')

    sudo('mkdir -p /var/log/uwsgi')
    sudo('chown uwsgi: /var/log/uwsgi')

    utils.upload_config_template('uwsgi.sh', '/etc/init.d/uwsgi', use_sudo=True)
    sudo('chmod +x /etc/init.d/uwsgi')
    sudo('update-rc.d uwsgi defaults')
    uwsgi_start()


@utils.run_as_sudo
def uwsgi_start():
    ''' Start uWSGI '''
    with settings(warn_only=True):
        sudo('/etc/init.d/uwsgi start')


@utils.run_as_sudo
def uwsgi_restart():
    ''' Restart uWSGI '''
    sudo('/etc/init.d/uwsgi restart')


@utils.run_as_sudo
def uwsgi_reload():
    ''' Start uWSGI '''
    sudo('/etc/init.d/uwsgi reload')