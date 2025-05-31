#!/usr/bin/env bash
# build.sh — exécute automatiquement les tâches Django sur Render

# Stop on error
set -o errexit

# Install dependencies (Render le fait déjà, mais tu peux forcer pip ici si besoin)
# pip install -r requirements.txt

# Migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

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
