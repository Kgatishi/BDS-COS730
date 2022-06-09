#from logging import _Level
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    level = models.IntegerField()
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=200)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)