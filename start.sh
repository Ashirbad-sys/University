#!/bin/bash
# Exit on any error
set -o errexit

echo "🚀 Starting Django project with Whitenoise & Gunicorn..."

# Apply database migrations
python manage.py migrate --noinput

# Collect static files for Whitenoise
python manage.py collectstatic --noinput

# Start Gunicorn with 4 workers (good for small Render instances)
gunicorn firstProject.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 4 \
    --threads 2 \
    --timeout 120
