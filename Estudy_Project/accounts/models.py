from calendar import c
from pyexpat import model
from django.db import models
# Create your models here.


class StudentUser(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
