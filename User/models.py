from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=50)
    username = models.CharField(primary_key=True, max_length=50, unique=True)

    def __str__(self):
        return self.username

class Post(models.Model):

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __string__(self):
        return self.user