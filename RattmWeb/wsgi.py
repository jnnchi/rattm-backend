"""
WSGI config for RattmWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
----------------------------------------------------------------------------------
-> WSGI := Web Server Gateway Interface
-> Specifications of an interface between web servers and web apps.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RattmWeb.settings')

application = get_wsgi_application()
