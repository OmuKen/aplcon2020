#!/bin/sh
cd manager
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations manager
python manage.py migrate
