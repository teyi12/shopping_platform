#!/usr/bin/env bash

python manage.py migrate --no-input
python manage.py collectstatic --no-input
