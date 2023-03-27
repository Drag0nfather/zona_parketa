# -*- coding: utf-8 -*-
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u1991005/data/zona_parketa')
sys.path.insert(1, '/var/www/u1991005/data/zona_parketa/venv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'parquetework.settings'
application = get_wsgi_application()
