# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
from fabric.colors import green, red
from fabric.operations import local, prompt
from fabric.context_managers import lcd, settings, hide
from fabric.api import env
from fabric.utils import puts
from mysql import *
import config_writer
from util import usernames_of_unixgroup


BLANK_PROJECT_REPO = 'git://github.com/futurecolors/tinned-django.git'
BLANK_PROJECT_BRANCH_NAME = 'master'
BLANK_PROJECT_NAME = 'tinned-django'
DEVELOPERS_USERGROUP = 'fcolors'
DEVELOPERS = usernames_of_unixgroup(DEVELOPERS_USERGROUP)
DEV_DB_PASSWORD = config_writer.generate_password()
USERNAME = 'futurecolors'

def make_django_project(project_name=''):

    def hello():
        print (green('Создание репозитория с заготовкой Django-проекта', True))


    def get_project_name(project_name):
        if not project_name:
            return prompt('Введите имя нового проекта: ', validate=r'\w+')
        else:
            return project_name


    def get_ip():
        return prompt('Введите ip-адрес сервера: ', validate=r'\d+\.\d+\.\d+\.\d+')


    def get_server_name():
        return prompt('Введите домен сервера (domain.com): ', validate=r'(\w+\.)?\w+\.\w+')


    def success():
        print(green('Адрес репозитория нового проекта -> /var/git/{0}.git', True).format(env.project_name))

        
    def git_prepare():
        # Создаём пустой репозиторий для нового проекта
        with lcd('/var/git/'):
            local('mkdir {0}.git'.format(env.project_name))
            with lcd('{0}.git/'.format(env.project_name)):
                local('git init --bare')
                # Чмоды для группы и разрешение на пуш для группы
                local('sudo chmod -R g+ws *')
                local('git repo-config core.sharedRepository true')

        # Создаём локальный репозиторий, скопировав файлы из репозитория шаблона
        with lcd('/tmp/'):
            local('git clone {repo} --branch={branch} {dir}'.format(repo=BLANK_PROJECT_REPO,
                                                                    branch=BLANK_PROJECT_BRANCH_NAME,
                                                                    dir=env.project_name))
            env.working_dir = '/tmp/{0}/{1}/'.format(project_name, BLANK_PROJECT_NAME)
            local('rm -rf {0}/.git'.format(env.project_name))

        config_writer.write_db_settings('production')
        config_writer.write_db_settings('staging')

        config_writer.write_fabfile()
        config_writer.write_project_name_in_сss()
        config_writer.write_secret_key()
        config_writer.create_settings_per_developer(DEVELOPERS, DEV_DB_PASSWORD)

        with lcd('/tmp/{0}/{1}'.format(env.project_name, BLANK_PROJECT_NAME)):
            # Конфигурируем локальные имена для коммита
            local('git config --global user.email "{0}@fc"'.format(env.user))
            local('git config --global user.name "{0}"'.format(env.user))

            local('git init')

            # Коммитим изменения в локальный репозиторий
            local('git add .')
            local('git commit -m "INITIAL"')

            # Связываем локальный и публичный репозитории
            local('git remote add origin /var/git/{0}.git/'.format(env.project_name))

            # Создаём ветку dev
            local('git checkout -b dev')

            # Пушим ветки из локального репозитория в общий
            local('git push --all')

        # Удаляем временный репозиторий
        local('rm -rf /tmp/{0}/'.format(env.project_name))


    hello()

    env.project_name = get_project_name(env.project_name)
    env.server_ip = get_ip()
    env.server_name = get_server_name()

    git_prepare()
    mysql.create_dbs_and_users(DEVELOPERS, DEV_DB_PASSWORD)

    success()