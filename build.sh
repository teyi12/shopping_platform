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
