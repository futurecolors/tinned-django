# coding: utf-8
import os


def get_redis_db():
    """ Separating developer dbs in redis based on their account uids
        This is kinda hacky, but suites our needs.
    """
    return os.getuid() - 1000
