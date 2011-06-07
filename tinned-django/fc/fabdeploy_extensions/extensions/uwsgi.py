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
            run('pip install uwsgi')


@utils.run_as_sudo
def uwsgi_setup():
    """ Setups uWSGI. """
    run('adduser --system --no-create-home --disabled-login --disabled-password --group uwsgi')

    run('mkdir -p /var/log/uwsgi')
    run('chown uwsgi: /var/log/uwsgi')

    utils.upload_config_template('uwsgi.sh', '/etc/init.d/uwsgi')
    run('chmod +x /etc/init.d/uwsgi')
    run('update-rc.d uwsgi defaults')
    uwsgi_start()


@utils.run_as_sudo
def uwsgi_start():
    ''' Start uWSGI '''
    run('/etc/init.d/uwsgi start')


@utils.run_as_sudo
def uwsgi_restart():
    ''' Restart uWSGI '''
    run('/etc/init.d/uwsgi restart')


@utils.run_as_sudo
def uwsgi_reload():
    ''' Start uWSGI '''
    run('/etc/init.d/uwsgi reload')