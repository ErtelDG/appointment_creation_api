@echo off

rem Führe die Migrations aus
python manage.py makemigrations
python manage.py migrate

rem Starte den Django-Server
python manage.py runserver