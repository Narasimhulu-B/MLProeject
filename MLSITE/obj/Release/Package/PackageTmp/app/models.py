"""
Definition of models.
"""
#from __future__ import unicode_literals
from django.db import models

# Create your models here.

class RP_USER_PROFILE(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    uesr_password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)
    class Meta:
        db_table = 'RP_USER_PROFILE'


class AUTH_USER(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    last_login=models.DateField()
    class Meta:
        db_table='AUTH_USER'
