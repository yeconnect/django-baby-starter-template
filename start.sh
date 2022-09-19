#!/usr/bin/env bash
echo migration start
python manage.py migrate --settings=settings.production
echo migration end
gunicorn config.wsgi:application --bind 0.0.0.0:8080