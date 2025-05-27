#!/bin/bash

# Appliquer les migrations
python manage.py migrate --noinput

# Collecter les fichiers statiques pour Whitenoise
python manage.py collectstatic --noinput

# Lancer le serveur avec gunicorn
exec gunicorn shopping_platform.wsgi:application --bind 0.0.0.0:$PORT
