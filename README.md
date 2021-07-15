# tradexa

This Application is written in:
Python 3.8
Django 3.2

I used class based views.

This application has two apps: User and Product
and each of them uses two diffrent sqlite databases.

There are two models for users:
User - first_name, last_name, email, password, username
Post - user, text, created_at, updated_at

And one model for Products
Product : name, weight, price, created_at, updated_at

Created forms with templates for user to create a post


## Execution:
Just Run ```sh commands.sh``` if you are on bash shell.
OR
Install the requirements:
```
pip install -r requirements.txt
```

Create the migrations (creates SQL commands)
```
python manage.py makemigrations
```

Run the migrations (Executes SQL commands)
```
python manage.py migrate --database=User_db
python manage.py migrate --database=Product_db
```
Create the superuser
```
python manage.py createsuperuser --database=User_db
```
And finaly run the server
```
python manage.py runserver
```

### Exception

No such table
Try deleting the database and recreate it using
```
python manage.py migrate --database=User_db  --run-syncdb
python manage.py migrate --database=Product_db  --run-syncdb
```
to see weather the database is created or not.
