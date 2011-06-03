# -*- coding: utf-8 -*-

from fabric.colors import green, red
from fabric.operations import local, prompt
from fabric.context_managers import lcd, settings, hide
from fabric.api import env
from fabric.utils import puts
from random import choice
import re

BLANK_PROJECT_REPO = 'git://github.com/futurecolors/tinned-django.git'
BLANK_PROJECT_BRANCH_NAME = 'master'
BLANK_PROJECT_NAME = 'tinned-django'
GROUP_FOR_PARSE = 'fcolors'

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

    hello()
    project_name = get_project_name(project_name)
    server_ip = get_ip()
    server_name = get_server_name()

    def get_group_users():
        group_file = local('cat /etc/group', capture=True)
        # Ищем строку в /etc/groups вида "groupname:x:1006:usr1,usr2,usr3",
        # чтобы создавать учётки для перечисленных в ней пользователей
        matches = re.search(GROUP_FOR_PARSE+':x:\d+:(?P<users>[\w,]+)', group_file)
        user_list = (matches.group(1)).split(',')
        return user_list

    def git_prepare():
        # Создаём пустой репозиторий для нового проекта
        with lcd('/var/git/'):
            local('mkdir {0}.git'.format(project_name))
            with lcd('{0}.git/'.format(project_name)):
                local('git init --bare')
                # Чмоды для группы и разрешение на пуш для группы
                local('sudo chmod -R g+ws *')
                local('git repo-config core.sharedRepository true')

        # Создаём локальный репозиторий, скопировав файлы из репозитория шаблона
        with lcd('/tmp/'):
            local('git clone {repo} --branch={branch} {dir}'.format(repo=BLANK_PROJECT_REPO,
                                                                  branch=BLANK_PROJECT_BRANCH_NAME,
                                                                  dir=project_name))
            local('rm -rf {0}/.git'.format(project_name))

        make_fabfile()
        insert_project_name()
        generate_secret_key()
        create_user_sql_settings()

        with lcd('/tmp/{0}/{1}'.format(project_name, BLANK_PROJECT_NAME)):
            # Конфигурируем локальные имена для коммита
            local('git config --global user.email "{0}@fc"'.format(env.user))
            local('git config --global user.name "{0}"'.format(env.user))

            local('git init')

            # Коммитим изменения в локальный репозиторий
            local('git add .')
            local('git commit -m "INITIAL"')

            # Связываем локальный и публичный репозитории
            local('git remote add origin /var/git/{0}.git/'.format(project_name))

            # Создаём ветку dev
            local('git checkout -b dev')

            # Пушим ветки из локального репозитория в общий
            local('git push --all')

        # Удаляем временный репозиторий
        local('rm -rf /tmp/{0}/'.format(project_name))

    def make_fabfile():
        from jinja2 import Environment, FileSystemLoader
        jenv = Environment(loader=FileSystemLoader('/tmp/{0}/{1}/'.format(project_name, BLANK_PROJECT_NAME)))
        text = jenv.get_template('fabfile.py').render({'SERVER_IP': server_ip,
                                                       'SERVER_NAME': server_name,
                                                       'INSTANCE_NAME': project_name})
        
        f = open('/tmp/{0}/{1}/fabfile.py'.format(project_name, BLANK_PROJECT_NAME), 'w')
        f.write(text)


    def insert_project_name():
        replace_string_in_file({'{{ PROJECT_NAME }}': project_name},
                               ['/tmp/{0}/{1}/settings.py'.format(project_name, BLANK_PROJECT_NAME),
                                '/tmp/{0}/{1}/_static/css/admin.css'.format(project_name, BLANK_PROJECT_NAME),
                                '/tmp/{0}/{1}/_static/css/common.css'.format(project_name, BLANK_PROJECT_NAME),
                                '/tmp/{0}/{1}/_static/css/dashboard.css'.format(project_name, BLANK_PROJECT_NAME),
                                '/tmp/{0}/{1}/_static/css/typo.css'.format(project_name, BLANK_PROJECT_NAME),
                                '/tmp/{0}/{1}/_static/css/wrapper.css'.format(project_name, BLANK_PROJECT_NAME),])

    def generate_secret_key():
        secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        replace_string_in_file({'{{ SECRET_KEY }}': secret_key},
                               ['/tmp/{0}/{1}/settings.py'.format(project_name, BLANK_PROJECT_NAME)])

    def gen_db_password():
        gen_db_password = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(16)])
        return gen_db_password

    DB_PASSWORD = gen_db_password()
    GROUP_USERS = get_group_users()

    def create_user_sql_settings():
        sql_set_template = """DATABASES = {{
        'default': {{
        'NAME': '{0}',
        'ENGINE': 'django.db.backends.mysql',
        'USER': '{1}',
        'PASSWORD': '{2}',
        'HOST': 'localhost',
        'OPTIONS': {{'init_command': 'SET storage_engine=INNODB'}}
            }}
        }}
        """
        with lcd('/tmp/{0}/{1}/_settings/environment/users/'.format(project_name, BLANK_PROJECT_NAME)):
            for user in GROUP_USERS:
                db_name = user_acc = '{0}_{1}'.format(project_name, user)
                sql_set = sql_set_template.format(db_name, project_name, DB_PASSWORD)
                local('echo "{0}" > {1}.py'.format(sql_set, user))

    def replace_string_in_file(replacement, file_names):
        for file_name in file_names:
            try:
                with open(file_name, 'r+') as file:
                    file_content = file.read()
                    for search, replace in replacement.items():
                        file_content = file_content.replace(search, replace)
                with open(file_name, 'w') as file:
                    file.write(file_content)
            except IOError as e:
                print red('Ошибка при замене в файле {0}: {2} (код {1})'.format(file_name, *e))

    def success():
        print(green('Адрес репозитория нового проекта -> /var/git/{0}.git', True).format(project_name))

#
# MySQL Part of Magic
#

    MYSQL_USER_EXISTS = "SHOW GRANTS FOR '{0}'@localhost;"
    MYSQL_BASE_EXISTS = "USE {0}_{1};"
    MYSQL_CREATE_DB = "CREATE DATABASE {0}_{1} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
    MYSQL_CREATE_USER = "CREATE USER '{0}'@'localhost' IDENTIFIED BY '{1}';"
    MYSQL_GRANT_PERMISSIONS = "GRANT ALL ON {0}.* TO '{1}'@'localhost'; FLUSH PRIVILEGES;"

    def mysql_execute(sql, user):
        sql = sql.replace('"', r'\"')
        return local('echo "%s" | mysql --user="%s"' % (sql, user))

    def mysql_user_exists(user):
        sql = MYSQL_USER_EXISTS.format(user)
        with settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
            result = mysql_execute(sql, 'root')
        return result.succeeded

    def mysql_base_exists(user):
        sql = MYSQL_BASE_EXISTS.format(project_name, user)
        with settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
            result = mysql_execute(sql, 'root')
        return result.succeeded

    def mysql_create_db(user):
        if mysql_base_exists(user):
            puts('База {0}_{1} уже существует. PASS'.format(project_name, user))
            return
        sql = MYSQL_CREATE_DB.format(project_name, user)
        mysql_execute(sql, 'root')

    def mysql_create_user(user):
        if mysql_user_exists(user):
            puts('Учётная запись для {0} уже существует. PASS'.format(user))
            return
        sql = MYSQL_CREATE_USER.format(project_name, DB_PASSWORD)
        mysql_execute(sql, 'root')

    def mysql_grant_permissions(user):
        db_name = "{0}_{1}".format(project_name, user)
        sql = MYSQL_GRANT_PERMISSIONS.format(db_name, project_name)
        mysql_execute(sql, 'root')

#
# Run, Script, Run!
#

    git_prepare()

    for user in GROUP_USERS:
        mysql_create_user(user)
        mysql_create_db(user)
        mysql_grant_permissions(user)

    success()