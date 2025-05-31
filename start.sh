#!/usr/bin/env bash
# start.sh — point d'entrée principal pour Render

# Stop on error
set -o errexit

# Migrations et collectstatic
python manage.py migrate
python manage.py collectstatic --no-input

# Création d'un superuser (optionnel)
if [[ "$CREATE_SUPERUSER" == "true" ]]; then
  python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(
        '$DJANGO_SUPERUSER_USERNAME',
        '$DJANGO_SUPERUSER_EMAIL',
        '$DJANGO_SUPERUSER_PASSWORD'
    )
END
fi

# Lancer Gunicorn
gunicorn shopping_platform.wsgi:application --bind 0.0.0.0:$PORT
