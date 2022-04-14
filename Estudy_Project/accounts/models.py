from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField('First Name', max_length=30, null=True, blank=True)
    Last_Name = models.CharField('Last Name', max_length=30, null=True, blank=True)
    Code = models.CharField('Code', max_length=30, null=True, blank=True)
    ID_Number = models.CharField('Id Number', max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return str(self.user)

class Lecturer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField('First Name', max_length=30, null=True, blank=True)
    Last_Name = models.CharField('Last Name', max_length=30, null=True, blank=True)
    Courses = models.CharField('Courses', max_length=30, null=True, blank=True)
    ID_Number = models.CharField('Id Number', max_length=30, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Lecturers"

    def __str__(self):
        return str(self.user)