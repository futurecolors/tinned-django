# -*- coding: utf-8 -*-
from fc.fabdeploy_extensions import start_project
from _settings.environment.production import DATABASES as production_db
from _settings.environment.staging import DATABASES as staging_db


def production():
    env.hosts = ['{{ USERNAME }}@{{ SERVER_IP }}']
    env.conf = dict(
        SERVER_NAME             = '{{ SERVER_NAME }}',
        INSTANCE_NAME           = '{{ INSTANCE_NAME }}',
        SUDO_USER               = '{{ USERNAME }}',
        NAME                    = 'production',
        DB_NAME                 = production_db['default']['NAME'],
        DB_USER                 = production_db['default']['USER'],
        DB_PASSWORD             = production_db['default']['PASSWORD'],
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


def staging():
    env.hosts = ['{{ USERNAME }}@{{ SERVER_IP }}']
    env.conf = dict(
        SERVER_NAME             = 'staging.{{ SERVER_NAME }}',
        INSTANCE_NAME           = '{{ INSTANCE_NAME }}_staging',
        SUDO_USER               = '{{ USERNAME }}',
        NAME                    = 'staging',
        DB_NAME                 = staging_db['default']['NAME'],
        DB_USER                 = staging_db['default']['USER'],
        DB_PASSWORD             = staging_db['default']['PASSWORD'],
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

def stable():
    return staging()