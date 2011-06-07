# -*- coding: utf-8 -*-
from _settings.environment.production import DATABASES as prod_databases

def production():
    env.hosts = ['futurecolors@{{ SERVER_IP }}']
    env.conf = dict(
        SERVER_NAME             = '{{ SERVER_NAME }}',
        INSTANCE_NAME           = '{{ INSTANCE_NAME }}',
        SUDO_USER               = 'futurecolors',
        NAME                    = 'production',
        DB_NAME                 = prod_databases['default']['NAME'],
        DB_USER                 = prod_databases['default']['USER'],
        DB_PASSWORD             = prod_databases['default']['PASSWORD'],
        DB_ROOT_PASSWORD        = '{{ DB_ROOT_PASSWORD }}',
        VCS                     = 'git',
        GIT_BRANCH              = 'master',
        LOCAL_CONFIG            = '__init__.py',
        REMOTE_CONFIG_TEMPLATE  = '__init__.py',
        PIP_REQUIREMENTS_PATH   = '_settings/fab_deploy/reqs',
        PIP_REQUIREMENTS_ACTIVE = 'active.txt',
        CONFIG_TEMPLATES_PATHS  = ['_settings/fab_deploy/config_templates'],
        OS                      = 'squeeze',
    )
    update_env()

def prod():
    return production()