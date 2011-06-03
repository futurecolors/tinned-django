from fabric.api import run, env, settings
from fab_deploy import utils
from fab_deploy import system
from fab_deploy import apache


__all__ = ['nginx_install', 'nginx_setup', 'nginx_restart', 'nginx_start']


@utils.run_as('root')
def nginx_install():
    """ Installs nginx. """
    os = utils.detect_os()
    options = {'squeeze': '-t testing'}
    system.aptitude_install('nginx-full', options.get(os, ''))
    run('rm -f /etc/nginx/sites-enabled/default')


@utils.run_as('root')
def nginx_setup():
    """ Updates nginx config and restarts nginx. """
    name = env.conf['INSTANCE_NAME']
    utils.upload_config_template('nginx.config', '/etc/nginx/sites-available/%s' % name)
    with settings(warn_only=True):
        run('ln -s /etc/nginx/sites-available/%s /etc/nginx/sites-enabled/%s' % (name, name))
    run('invoke-rc.d nginx reload')


@utils.run_as('root')
def nginx_restart():
    run('invoke-rc.d nginx reload')


@utils.run_as('root')
def nginx_start():
    run('invoke-rc.d nginx start')