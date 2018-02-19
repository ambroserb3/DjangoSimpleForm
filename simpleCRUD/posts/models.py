# Create your models here.
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    """
    Creates instances of a `User`.
    """

    first_name = models.CharField(max_length=50) # CharField is field type for characters
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=22)
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
