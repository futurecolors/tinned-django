# coding: utf-8


class CelerySettings(object):
    BROKER_BACKEND = "redis"
    BROKER_HOST = "localhost"
    BROKER_PORT = 6379
    BROKER_USER = ""
    BROKER_PASSWORD = ""
    BROKER_VHOST = "5"

    CELERY_RESULT_BACKEND = "database"
    CELERY_IGNORE_RESULT = False
    CELERY_TRACK_STARTED = True

    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 2
    REDIS_CONNECT_RETRY = True

    CELERY_SEND_EVENTS = True
    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"