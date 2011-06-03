# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.query import QuerySet
import copy
import logging


logger = logging.getLogger('debug')


if settings.DEBUG and settings.FIRELOGGER:
    def fp(*args, **kwargs):
        """Выводит указанные аргументы в консоли FirePython. Принимает произвольное
        количество аргументов, ключ именнованных параметров выводится как метка.
        Можно указать именованный параметр level для указания уровня сообщения
        (по умолчанию info)"""
        log_method = logger.info
        if 'level' in kwargs:
            log_method = getattr(logger, kwargs['level'])
        tpl = []
        vars = []
        # боремся с вызовом функции после изменения объекта
        copy_args = copy.deepcopy(args)
        copy_kwargs = copy.deepcopy(kwargs)
        for arg in copy_args:
            tpl += ['%s']
            # боремся с lazy-loading
            if not isinstance(arg, QuerySet):
                vars += [arg]
            else:
                vars += [list(arg)]
        for arg in copy_kwargs:
            if 'level' != arg:
                tpl += ['%s: %s']
                vars += arg, kwargs[arg]
        log_method("\n".join(tpl), *vars)
else:
    def fp(*args, **kwargs):
        pass


# Добавляем fp во встроенные функции
__builtins__['fp'] = fp