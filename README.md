# Описание проекта
Данный проект - веб-сайт на Django 3.2.15, предназначенный для менторов и их "менти". Сайт предоставляет инструменты для коммуникации, наставничества и обмена знаниями между менторами и "менти".

# Установка и запуск
Склонируйте репозиторий на локальный компьютер:
git clone https://github.com/username/repo.git

Для запуска данного проекта необходимо иметь на компьютере установленный Python 3
python -m venv venv

.\venv\Scripts\activate on Windows

source /venv/bin/activate on Linux


Установите необходимые зависимости:
pip install -r requirements.txt

Перейдите в корневую папки проекта:
cd django-website
cd src

Создайте базу данных:
python manage.py migrate

Запустите сервер:
python manage.py runserver

Перейдите по адресу:
http://127.0.0.1:8000/

# Структура проекта
Структура проекта выглядит следующим образом:
apps/ - директория, содержащая код приложения

static/ - директория, содержащая статические файлы (CSS, JS, изображения)

templates/ - директория, содержащая шаблоны HTML-страниц

__init__.py - файлы-индикаторы, сообщающие Python, что данная директория является пакетом

apps.py - файлы, содержащие конфигурацию приложения

models.py - файлы, содержащие определения моделей базы данных

urls.py - файлы, содержащие маршруты приложения

views.py - файлы, содержащие представления (views) для приложения

# Использованные технологии
Django 3.2.15 - веб-фреймворк для создания веб-приложений на языке Python

HTML - язык разметки веб-страниц

CSS - язык описания внешнего вида веб-страниц

SQLite - легковесная реляционная база данных, используемая в данном проекте в качестве базы данных
