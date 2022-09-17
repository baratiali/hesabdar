from __future__ import unicode_literals #__future__ is a module that allows you to use new features of Python 3 in Python 2.7

from django.db import models # django.db is a database API for Python
from django.contrib.auth.models import User # django.contrib.auth.models is a module that contains the User model

# Create your models here.

class Expense(models.Model): # models.Model is a class that contains all the fields and behaviors of the model
    user = models.ForeignKey(User, on_delete=models.CASCADE) # foreingkey is a field that creates a one-to-many relationship between two models
    amount = models.IntegerField()# model.intergerfield is a field that stores an integer
    text = models.CharField(max_length=200) # charfield is a field that stores a string
    date = models.DateTimeField()

    def __str__(self): # __str__ is a method that returns a string representation of an object
        return self.text 

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    text = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.text
 