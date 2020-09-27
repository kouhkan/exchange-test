#!/bin/sh
cd /code
su  -c "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py loaddata db.json && gunicorn --workers=2 A.wsgi -b 0.0.0.0:8080"

