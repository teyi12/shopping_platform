import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_platform.settings')

application = get_wsgi_application()
"""
WSGI config for shopping_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Définir le module de configuration des paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_platform.settings')

application = get_wsgi_application()
