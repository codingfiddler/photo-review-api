#!/usr/bin/env bash
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8888
