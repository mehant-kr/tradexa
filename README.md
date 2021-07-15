# tradexa

This Application is written in:<br>
Python 3.8<br>
Django 3.2

I used class based views.

This application has two apps: User and Product
and each of them uses two diffrent sqlite databases.

__Two Databases__: <br>
User_db stores
- auth_user, sessions, User_post, User_user <br>

Product_db stores
- Product_product

There are two models for users: <br>
User - first_name, last_name, email, password, username <br>
Post - user, text, created_at, updated_at<br>

And one model for Products<br>
Product : name, weight, price, created_at, updated_at

Created forms with templates for authenticated user to create a post


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

`No such table` <br>
Try deleting the database and recreate it using
```
python manage.py migrate --database=User_db  --run-syncdb
python manage.py migrate --database=Product_db  --run-syncdb
```
to see weather the database is created or not.
