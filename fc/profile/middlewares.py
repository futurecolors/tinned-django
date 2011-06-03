# -*- coding: utf-8 -*-
import sys
from django.conf import settings
from django.db import connection
from django.shortcuts import redirect
from annoying.exceptions import Redirect
from firepython.middleware import FirePythonDjango


class FcFirePythonDjango(FirePythonDjango):
    '''Костыль из-за конфликта с annoying.middlewares.RedirectMiddleware'''
    def _simple_sql_debug(self):
        total_queries = len(connection.queries)

        if settings.DEBUG_TOOLBAR_ENABLED:
            total_sql_time = round(sum([query.get('duration', 0) for query in connection.queries]), 2)
        else:
            total_sql_time = 'very inaccurate (enable Debug toolbar)' + str(round(sum([float(query['time']) for query in connection.queries]), 2))

        for query in connection.queries:
            level = 'warning' if query.get('is_slow') else 'debug'
            time = query.get('time', query.get('duration'))
            fp(query['sql'], time, level=level)
        fp('{0} SQL queries in {1} ms'.format(total_queries, total_sql_time), level='info')

    def process_response(self, request, response):
        if settings.FIREPYTHON_SQL:
            self._simple_sql_debug()

        if sys.exc_type:
            if isinstance(sys.exc_value, Redirect):
                return redirect(*sys.exc_value.args)
        return super(FcFirePythonDjango, self).process_response(request, response)