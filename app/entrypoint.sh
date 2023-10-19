#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn app.wsgi --bind=0.0.0.0:8000