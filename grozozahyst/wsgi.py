"""
WSGI config for radioservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import site

site.addsitedir('/var/www/grozozahyst.com/lib/python2.7/site-packages')

import os, sys

from django.core.wsgi import get_wsgi_application
from django.conf import settings

sys.path.append('/var/www/grozozahyst.com/bin/grozozahyst')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grozozahyst.settings")

application = get_wsgi_application()