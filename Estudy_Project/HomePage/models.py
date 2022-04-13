
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(auto_now=True, auto_now_add=False)
    content = models.CharField(max_length=100)