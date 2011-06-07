# -*- coding: utf-8 -*-
from fabric.operations import local
from fabric.context_managers import lcd, settings, hide
from fabric.utils import puts

MYSQL_USER_EXISTS = "SHOW GRANTS FOR '{0}'@localhost;"
MYSQL_BASE_EXISTS = "USE {0}_{1};"
MYSQL_CREATE_DB = "CREATE DATABASE {0}_{1} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
MYSQL_CREATE_USER = "CREATE USER '{0}'@'localhost' IDENTIFIED BY '{1}';"
MYSQL_GRANT_PERMISSIONS = "GRANT ALL ON {0}.* TO '{1}'@'localhost'; FLUSH PRIVILEGES;"

def create_dbs_and_users(developers):
    for user in developers:
        mysql_create_user(user)
        mysql_create_db(user)
        mysql_grant_permissions(user)

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
