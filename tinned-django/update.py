#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

def update_commands():
    # Обновление окружения
    args = ['source', '../env/bin/activate']
    subprocess.call(args)
    args = ['pip', 'install', '-r', 'reqs.txt']
    subprocess.call(args)

    # Запуск syncdb
    args = ['python', 'manage.py', 'syncdb']
    subprocess.call(args)

    # Запуск миграций
    args = ['python', 'manage.py', 'migrate']
    subprocess.call(args)

    # Повторный syncdb чтобы появились права доступа из моделей
    args = ['python', 'manage.py', 'syncdb', '--all']
    subprocess.call(args)
    
    # Перезагружаем дев
    # Важно, что импорт происходит именно зедсь после установки пакетов
    import settings
    if settings.DEBUG:
        print 'Reloading uwsgi...'
        args = ['touch', '../reload.txt']
        subprocess.call(args)

    
if __name__ == '__main__':
    update_commands()