# based on https://docs.djangoproject.com/en/1.3/howto/deployment/modwsgi/

import os
import sys

path = '/path/to/rchangelog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'rchangelog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
