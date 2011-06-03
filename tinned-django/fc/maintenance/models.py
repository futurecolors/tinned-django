# coding: utf-8
from django.db import models


class Config(models.Model):
    key   = models.CharField(u'Ключ', max_length=255, unique=True)
    value = models.CharField(u'Значение', max_length=255, blank=True)

    @classmethod
    def is_maintenance(cls):
        try:
            maintenance = cls.objects.get(key='maintenance')
            return bool(int(maintenance.value))
        except cls.DoesNotExist:
            return False

    @classmethod
    def set_maintenance_state(cls, value):
        try:
            maintenance = cls.objects.get(key='maintenance')
        except cls.DoesNotExist:
            maintenance = cls()
            maintenance.key = 'maintenance'
        maintenance.value = '1' if value else '0'
        maintenance.save()