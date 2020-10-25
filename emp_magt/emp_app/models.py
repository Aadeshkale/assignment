from django.db import models

# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
