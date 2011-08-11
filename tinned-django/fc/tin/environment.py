# -*- coding: utf-8 -*-
from fabric.colors import green
from fabric.operations import local, prompt
from fabric.context_managers import lcd, settings, hide
import os
import socket
from fc.tin.config_writer import write_template
from fc.tin.util import usernames_unixgroup

DEVELOPERS_USERGROUP = 'uwsgi_test'
PROJECTS = []


def setup_environment():

    def _get_path_to_virtualenv(project, developer):
        return '/home/{developer}/projects/{project}/env/'.format(project=project, developer=developer)

    
    def get_socket_path(project, developer):
        return '/tmp/{0}.{1}.sock'.format(project, developer)


    def _create_project(name):
        local('sudo mkdir -p {0}'.format(name))
        with lcd(name):
            local('sudo mkdir -p src')
            local('sudo virtualenv --no-site-packages env')
            local('sudo touch reload.txt')


    def _write_root_config(outfilepath, relative_path, context, target_dir):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        write_template(filepath=os.path.join(current_dir, relative_path),
                       context=context,
                       outputfilepath=outfilepath)
        local('sudo mv {0} {1}'.format(outfilepath, target_dir))


    def _create_uwsgi_config(project, developer):
        context = {'SOCKET_PATH': get_socket_path(project, developer),
                   'PATH_TO_VIRTUALENV': _get_path_to_virtualenv(project, developer),
                   'PROJECT_PATH': os.path.join('/home', developer, 'projects', project, 'src'),
                   'RELOAD_TXT': os.path.join('/home', developer, 'projects', project, 'reload.txt'),
                   'USER': developer,
                   'GROUP': DEVELOPERS_USERGROUP}


    def _create_nginx_config(project, developer):
        context = {'SOCKET_PATH': get_socket_path(project, developer),
                   'SERVER_IP': socket.gethostbyname('{0}.{1}'.format(project, developer)),
                   'SERVER_NAME': '{0}.{1}'.format(project, developer)}
        _write_root_config(relative_path='configs/nginx.config',
                           context=context,
                           target_dir='/etc/nginx/fc/',
                           outfilepath = '/tmp/{0}.{1}'.format(project, developer))

        
    def _create_directory_layout(developers):
        for developer_name in developers:
            with lcd('/home/{0}'.format(developer_name)):
                local('sudo mkdir -p projects')
                with lcd('projects'):
                    for project in PROJECTS:
                        _create_project(project)
                        _create_uwsgi_config(project, developer_name)
                        _create_nginx_config(project, developer_name)
                local('sudo chown -R {user}:{group} /home/{user}/projects/'.format(user=developer_name, group=DEVELOPERS_USERGROUP))
                local('sudo chmod -R 755 /home/{user}/projects/'.format(user=developer_name))

        
    print (green('Создаём инфраструктуру для разработчиков', True))
    PROJECTS = prompt('Введите названия проектов через запятую: ', validate=r'[\w\,]+').split(',')
    DEVELOPERS = usernames_unixgroup(DEVELOPERS_USERGROUP)
    local('sudo mkdir -p /etc/uwsgi/')
    _create_directory_layout(DEVELOPERS)
    local('sudo /etc/init.d/nginx reload')