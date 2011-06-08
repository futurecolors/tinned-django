from fabric.api import run, sudo, env, settings
from fab_deploy import utils
from fab_deploy import system

__all__ = ['nginx_install', 'nginx_setup', 'nginx_restart', 'nginx_start']


@utils.run_as_sudo
def nginx_install():
    """ Installs nginx. """
    os = utils.detect_os()
    options = {'squeeze': '-t testing'}
    system.aptitude_install('nginx-full', options.get(os, ''))
    sudo('rm -f /etc/nginx/sites-enabled/default')


@utils.run_as_sudo
def nginx_setup():
    """ Updates nginx config and restarts nginx. """
    name = env.conf['INSTANCE_NAME']
    utils.upload_config_template('nginx.config', '/etc/nginx/sites-available/%s' % name, use_sudo=True)
    with settings(warn_only=True):
        sudo('ln -s /etc/nginx/sites-available/%s /etc/nginx/sites-enabled/%s' % (name, name))
    nginx_start()


@utils.run_as_sudo
def nginx_restart():
    sudo('invoke-rc.d nginx reload')


@utils.run_as_sudo
def nginx_start():
    sudo('invoke-rc.d nginx start')