#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate --database=User_db
python manage.py migrate --database=Product_db
python manage.py makemigrations
python manage.py createsuperuser --database=User_db
python manage.py runserver
