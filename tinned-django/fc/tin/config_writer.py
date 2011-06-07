# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import os
from random import choice
from fabric.api import env
from fabric.operations import local
from fabric.context_managers import lcd
from start_project import USERNAME

def write_template(file, context):
    jenv = Environment(loader=FileSystemLoader(dir))
    text = jenv.get_template(file).render(context)
    f = open(file, 'w')
    f.write(text.encode('UTF-8'))


def generate_password(length=10):
    db_password = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length)])
    return db_password


def write_db_settings(environment):
    write_template(os.path.join(env.working_dir, '_settings', 'environment', environment),
            {'DB_NAME': env.project_name,
             'DB_USER': USERNAME,
             'DB_PASSWORD': generate_password()})


def write_fabfile():
    write_template(os.path.join(env.working_dir, 'fabfile.py'),
            {'SERVER_IP': server_ip,
             'SERVER_NAME': server_name,
             'INSTANCE_NAME': project_name,
             'DB_ROOT_PASSWORD': db_root_password,
             'USERNAME': USERNAME})

    
def write_secret_key():
    write_template(os.path.join(env.working_dir, 'settings.py'),
            {'SECRET_KEY': generate_password(50)})


def write_project_name_in_css():
    dir = os.path.join(env.working_dir, '_static', 'css')
    for f in os.listdir(dir):
        if os.path.isfile(os.path.join(dirname, f)):
            write_template(os.path.join(dir, f), {'PROJECT_NAME': env.project_name})


def create_settings_per_developer(developers, password):
    sql_set_template = """DATABASES = {{
    'default': {{
    'NAME': '{DB_NAME}',
    'ENGINE': 'django.db.backends.mysql',
    'USER': '{DB_USER}',
    'PASSWORD': '{DB_PASSWORD}',
    'HOST': 'localhost',
    'OPTIONS': {{'init_command': 'SET storage_engine=INNODB'}}
        }}
    }}
    """
    with lcd(os.path.join(env.working_dir, '_settings', 'environment', 'users')):
        for user in developers:
            db_name  = '{0}_{1}'.format(env.project_name, user)
            sql_set = sql_set_template.format(dict(DB_NAME=db_name, DB_USER=env.project_name, DB_PASSWORD=password))
            local('echo "{0}" > {1}.py'.format(sql_set, user))