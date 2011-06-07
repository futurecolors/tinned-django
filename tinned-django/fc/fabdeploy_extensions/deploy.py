# -*- coding: utf-8 -*-
from fab_deploy import virtualenv, deploy, vcs, utils
from fabric.api import run, env, settings, hide, puts
from fabric.context_managers import cd
from fabric.contrib import console
from fabric.contrib import files
from fabric.utils import warn

import system
from extensions import chmod, uwsgi, nginx
import django_commands as dj_cmd


__all__ = ['full_deploy', 'deploy_project',
           'update_django_config', 'setup_web_server', 'push']


def full_deploy():
    """ Prepares server and deploys the project. """
    #TODO: install vim, mс
    system.prepare_server()
    deploy_project()

    chmod.set_chmod()
    dj_cmd.collectstatic()
    dj_cmd.compress()


def deploy_project():
    """ Deploys project on prepared server. """
    virtualenv.virtualenv_create()
    deploy.make_clone()
    virtualenv.pip_install(env.conf.PIP_REQUIREMENTS, restart=False)
    setup_web_server()
    
    dj_cmd.syncdb()
    dj_cmd.migrate()
    dj_cmd.collectstatic()
    dj_cmd.manage('compress')


def update_django_config(restart=True):
    files.upload_template(
        utils._project_path(env.conf.REMOTE_CONFIG_TEMPLATE),
        utils._remote_project_path(env.conf.LOCAL_CONFIG),
        env.conf, True
    )
    if restart:
        uwsgi.uwsgi_reload()


def setup_web_server():
    """ Sets up a web server (uwsgi + nginx). """
    uwsgi.uwsgi_install()
    nginx.nginx_install()

    nginx.nginx_setup()
    uwsgi.uwsgi_setup()


def push(*args, **kwargs):
    allowed_args = set(['notest', 'syncdb', 'migrate', 'pip_update', 'norestart'])
    for arg in args:
        if arg not in allowed_args:
            puts('Invalid argument: %s' % arg)
            puts('Valid arguments are: %s' % allowed_args)
            return

    vcs.push()
    utils.delete_pyc()
    with cd('src/' + env.conf['INSTANCE_NAME']):
        vcs.up()

    if 'pip_update' in args:
        virtualenv.pip_update(restart=False)
    if 'syncdb' in args:
        dj_cmd.syncdb()
    if 'migrate' in args:
        dj_cmd.migrate()

    dj_cmd.collectstatic()
    dj_cmd.manage('compress')

    # execute 'before_restart' callback
    kwargs.get('before_restart', lambda: None)()

    if 'norestart' not in args:
        uwsgi.uwsgi_reload()