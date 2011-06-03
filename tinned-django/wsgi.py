import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['DJANGO_SETTINGS_ENVIRONMENT'] = 'production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()