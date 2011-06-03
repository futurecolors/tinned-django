# -*- coding: utf-8 -*-
from fab_deploy import *
from fabric.context_managers import cd
from fabric.api import run, env
from _settings.environment.production import DATABASES as prod_databases
from fc.fabdeploy_extensions.deploy import make_django_project

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