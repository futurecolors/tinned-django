# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
    os.environ['DJANGO_CONFIGURATION'] = "Testing"

    from configurations.management import execute_from_command_line

    args = ['manage.py', 'test'] + sys.argv[1:]
    execute_from_command_line(args)