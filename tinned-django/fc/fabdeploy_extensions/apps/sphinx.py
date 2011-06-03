# -*- coding: utf-8 -*-
from fabric.api import run, settings, env, cd

from fab_deploy import utils
from fab_deploy.system import aptitude_install
from fab_deploy.django_commands import get_manage_py_command
from fab_deploy.crontab import crontab_update


__all__ = ['sphinx_setup', 'sphinx_config', 'sphinx_indexer', 'sphinx_start']


SPHINX_CONFIG = '/etc/sphinxsearch/sphinx.conf'


@utils.run_as('root')
def sphinx_setup():
    ''' Install sphinx search '''
    aptitude_install('sphinxsearch')
    run('sed -i "s/START=no/START=yes/g" /etc/default/sphinxsearch')


@utils.run_as('root')
@utils.inside_project
def sphinx_config(apps):
    ''' Generate sphinx config from django '''

    generate_command = get_manage_py_command('generate_sphinx_config')
    run('{0} {1} > {2}'.format(generate_command, apps, SPHINX_CONFIG))

    make_log_files()
    sphinx_indexer()
    sphinx_start()


@utils.run_as('root')
def make_log_files():
    ''' Generate sphinx config from django '''
    sphinx_config = run('cat {0}'.format(SPHINX_CONFIG))
    for line in sphinx_config.splitlines():
        option = line.replace(' ', '').split('=')
        if len(option) == 2 and option[1].endswith('.log'):
            run('touch {0}'.format(option[1]))


@utils.run_as('root')
def sphinx_indexer():
    ''' Setup sphinx indexing '''
    indexer_command = 'indexer --all --rotate >/dev/null 2>&1'
    run(indexer_command)
    crontab_update('0-59 * * * * {0}'.format(indexer_command), 'indexer')


@utils.run_as('root')
def sphinx_start():
    ''' Run sphinx daemon '''
    run('/etc/init.d/sphinxsearch start')