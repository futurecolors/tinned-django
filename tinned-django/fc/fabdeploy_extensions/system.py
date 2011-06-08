# -*- coding: utf-8 -*-
from fab_deploy import utils, mysql, system
from fabric.api import run, env, settings, hide, sudo
from fabric.utils import warn
from fabric import utils as fabric_utils
from extensions import redis


def prepare_server():
    """ Prepares server: installs system packages. """
    os = utils.detect_os()
    if os in ['lenny', 'squeeze']:
        system.install_sudo()

    system.setup_backports()
    setup_testing_sources()

    mysql.mysql_install()
    with settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
        mysql.mysql_create_db()
    system.install_common_software()
    redis.redis_install()
    redis.redis_setup()


@utils.run_as_sudo
def setup_testing_sources():
    """ Adds testing yandex repo to apt sources. """
    os = utils.detect_os()
    debian_repo = 'http://mirror.yandex.ru'
    testing = {
        'squeeze': '{0}/debian wheezy main non-free contrib'.format(debian_repo),
    }

    if os not in testing:
        fabric_utils.puts("Testing sources are not available for " + os)
        return

    sudo("echo 'deb %s' > /etc/apt/sources.list.d/wheezy.list" % testing[os])
    with settings(warn_only=True):
        run('aptitude update')