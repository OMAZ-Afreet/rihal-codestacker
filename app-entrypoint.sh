#!/bin/sh

echo "Database migrations ... "
python manage.py makemigrations
python manage.py migrate
echo "Migrations DONE. "


echo "Running server ... "
gunicorn -w 2 -b 0.0.0.0:8000 pdf_search.wsgi

