from fabric.api import run
from fab_deploy import utils
from fab_deploy import system


@utils.run_as_sudo
def redis_install():
    """ Installs Redis """
    os = utils.detect_os()
    options = {'squeeze': '-t testing'}
    system.aptitude_install('redis-server', options.get(os, ''))

@utils.run_as_sudo
def redis_setup():
    """ Setups Redis """
    utils.upload_config_template('redis.conf', '/etc/redis/redis.conf')
    run('update-rc.d redis-server defaults')
    redis_restart()

@utils.run_as_sudo
def redis_start():
    ''' Start redis '''
    run('/etc/init.d/redis-server start')

@utils.run_as_sudo
def redis_restart():
    ''' Restart redis '''
    run('/etc/init.d/redis-server restart')