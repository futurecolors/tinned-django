# -*- coding: utf-8 -*-
from fab_deploy import *
from fabric.context_managers import cd
from fabric.api import run, env
from _settings.environment.production import DATABASES as prod_databases
from fc.fabdeploy_extensions.start_project import make_django_project
from fc.fabdeploy_extensions.apps import chmod, uwsgi
from fabric.contrib import files

def prod():
    env.hosts = ['futurecolors@{{ SERVER_IP }}']
    env.conf = dict(
        SERVER_NAME             = '{{ SERVER_NAME }}',
        INSTANCE_NAME           = '{{ INSTANCE_NAME }}',
        NAME                    = 'production',
        DB_NAME                 = prod_databases['default']['NAME'],
        DB_USER                 = prod_databases['default']['USER'],
        DB_PASSWORD             = prod_databases['default']['PASSWORD'],
        VCS                     = 'git',
        GIT_BRANCH              = 'master',
        REMOTE_CONFIG_TEMPLATE  = 'settings.py',
        PIP_REQUIREMENTS_PATH   = '_settings/fab_deploy/reqs',
        PIP_REQUIREMENTS_ACTIVE = 'active.txt',
        CONFIG_TEMPLATES_PATHS  = ['_settings/fab_deploy/config_templates'],
        OS                      = 'squeeze',
    )
    update_env()

    
def full_deploy():
    #TODO: install vim, mc
    mysql.mysql_install()
    mysql.mysql_create_db()
    deploy.full_deploy()
    chmod.set_chmod()
    dj_cmd.collectstatic()
    dj_cmd.compress()


def prepare_server():
    """ Prepares server: installs system packages. """
    os = utils.detect_os()
    if os in ['lenny', 'squeeze']:
        install_sudo()

    setup_backports()
    fc_setup_testing_sources()
    install_common_software()

    
@utils.run_as('root')
def fc_setup_testing_sources():
    """ Adds testing repo to apt sources. """
    os = utils.detect_os()
    debian_repo = 'http://mirror.yandex.ru'
    testing = {
        'squeeze': '{0}/debian wheezy main non-free contrib'.format(debian_repo),
    }

    if os not in testing:
        fabric_utils.puts("Testing sources are not available for " + os)
        return

    run("echo 'deb %s' > /etc/apt/sources.list.d/wheezy.list" % testing[os])
    with settings(warn_only=True):
        run('aptitude update')

        
def update_django_config(restart=True):
    files.upload_template(
        utils._project_path(env.conf.REMOTE_CONFIG_TEMPLATE),
        utils._remote_project_path(env.conf.LOCAL_CONFIG),
        env.conf, True
    )
    if restart:
        uwsgi.uwsgi_reload()


def push(*args, **kwargs):
    deploy.push(*args, **kwargs)
    if 'norestart' not in args:
        uwsgi.uwsgi_reload()


def setup_web_server():
    """ Sets up a web server (uwsgi + nginx). """
    uwsgi.uwsgi_install()
    nginx.nginx_install()

    nginx.nginx_setup()
    uwsgi.uwsgi_setup()