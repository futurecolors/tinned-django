# -*- coding: utf-8 -*-
from fab_deploy import utils, mysql
from fabric.api import run, env, settings, hide
from fabric.utils import warn


__all__ = ['migrate', 'manage', 'syncdb', 'compress', 'collectstatic',
           'command_is_available']


@utils.inside_project
def command_is_available(command):
    with settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
        output = run('DJANGO_SETTINGS_ENVIRONMENT={0} python manage.py help {1}'.format(env.conf['NAME'], command))

    if output.succeeded:
        return True

    # that's ugly
    unknown_command_msg = "Unknown command: '%s'" % command
    if unknown_command_msg in output:
        return False

    # re-raise the original exception
    run('DJANGO_SETTINGS_ENVIRONMENT={0} python manage.py help {1}'.format(env.conf['NAME'], command))


@utils.inside_project
def manage(command):
    """ Runs django management command. DJANGO_SETTINGS_ENVIRONMENT is preset
    Example::

        fab manage:createsuperuser
    """

    command_name = command.split()[0]
    if not command_is_available(command_name):
        warn('Management command "%s" is not available' % command_name)
    else:
        run('DJANGO_SETTINGS_ENVIRONMENT={0} python manage.py {1}'.format(env.conf['NAME'], command))


def migrate(params='', do_backup=False):
    """ Runs migrate management command. Database backup is performed
    before migrations if ``do_backup=False`` is not passed. """
    if do_backup:
        backup_dir = env.conf['ENV_DIR'] + '/var/backups/before-migrate'
        run('mkdir -p ' + backup_dir)
        with settings(warn_only=True):
            mysql.mysqldump(backup_dir)
    manage('migrate --noinput %s' % params)


def syncdb(params=''):
    """ Runs syncdb management command. """
    manage('syncdb --noinput %s' % params)


def collectstatic(params=''):
    ''' Collect staticfiles Django 1.3 '''
    with settings(warn_only=True):
        manage('collectstatic --noinput %s' % params)


def compress(params=''):
    ''' Django-compressor '''
    with settings(warn_only=True):
        manage('synccompress %s' % params)