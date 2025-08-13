#!/bin/bash
# Exit if any command fails
set -o errexit  

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn server
gunicorn firstProject.wsgi:application --bind 0.0.0.0:$PORT
