"""
    Default wsgi.py for django-configurations
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()