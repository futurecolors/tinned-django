# coding: utf-8
from apps.utils.redis import get_redis_db
import celery_redis_unixsocket  # it's important for monkey-patching


class CelerySettings(object):
    # Fix it after upgrade to kombu>=3.0 (currently incompatible with django-celery)
    # celery_redis_unixsocket won't be necessary anymore too.
    # BROKER_URL = 'redis+socket:///var/run/redis/{{ project_name }}.sock/1'
    # CELERY_RESULT_BACKEND = BROKER_URL

    BROKER_TRANSPORT = 'celery_redis_unixsocket.broker.Transport'
    BROKER_HOST = '/var/run/redis/{{ project_name}}.sock'
    BROKER_VHOST = 1

    CELERY_IGNORE_RESULT = False
    CELERY_RESULT_BACKEND = 'redisunixsocket'
    CELERY_REDIS_HOST = BROKER_HOST

    CELERY_SEND_EVENTS = True
    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"


class CeleryDevSettings(object):
    BROKER_VHOST = get_redis_db()
