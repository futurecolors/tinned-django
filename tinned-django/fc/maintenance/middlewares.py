# coding: utf-8
from django.core.urlresolvers import resolve, Resolver404
from django.conf import settings
import settings as maintenance_settings
from views import maintenance
from models import Config
import re


# Настройки
MAINTENANCE_SITE_ENABLED = getattr(settings, 'MAINTENANCE_SITE_ENABLED',
                                   maintenance_settings.MAINTENANCE_SITE_ENABLED)
MAINTENANCE_WARNING      = getattr(settings, 'MAINTENANCE_WARNING',
                                   maintenance_settings.MAINTENANCE_WARNING)


def _is_admin(request):
    try:
        return resolve(request.path).app_name == 'admin'
    except Resolver404:
        return False


class MaintenanceMiddleware():
    ''' Ошибка 503'''
    def is503(self):
        if not hasattr(self, '_is503'):
            self._is503 =  Config.is_maintenance() or not MAINTENANCE_SITE_ENABLED
        return self._is503

    def process_view(self, request, view_func, view_args, view_kwargs):
        if self.is503() and not request.user.is_staff:
            return maintenance(request)

    def process_response(self, request, response):
        if _is_admin(request) and hasattr(self, '_is503'):
            del self._is503 # Сбрасываем "кеш", так он мог устареть
        if self.is503() and request.user.is_staff:
            response.content = re.sub(r'<body.*>',
                                      '\g<0>' + MAINTENANCE_WARNING,
                                      response.content)
        return response