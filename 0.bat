@echo off
call Scripts\activate
cd challenge_1
start http://127.0.0.1:8000/
python manage.py runserver


