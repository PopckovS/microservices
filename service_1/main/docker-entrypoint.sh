#!/bin/bash

echo "Применяем миграции"
python manage.py migrate

echo "Запускаем фикстуры"
python manage.py loaddata fixtures/*

echo "Запуск сервера"
python manage.py runserver 0.0.0.0:8000

#Сделать выгрузку суперпользователя
#python manage.py dumpdata auth.user  --indent 2 > fixtures/auth_user.json


#Применяем миграции
#Operations to perform:
#  Apply all migrations: admin, auth, contenttypes, front, sessions
#Running migrations:
#  Applying front.0001_add_news_and_category... OK
#Запускаем фикстуры
#Installed 1 object(s) from 1 fixture(s)
#Запуск сервера
#Watching for file changes with StatReloader
#Performing system checks...
#
#System check identified no issues (0 silenced).
#January 05, 2022 - 02:08:10
#Django version 3.2.10, using settings 'main.settings'
#Starting development server at http://0.0.0.0:8000/
#Quit the server with CONTROL-C.


