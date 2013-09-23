#!/usr/bin/env python
"""
    Default manage.py for django-configurations
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        os.environ['DJANGO_CONFIGURATION'] = 'Testing'

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
