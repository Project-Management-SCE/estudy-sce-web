from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

DEPARTMENT_CHOICES = (
    ("1","הנדסת תוכנה"),
    ("2","הנדסת בניין"),
    ("3","הנדסת מכונות"),
    ("4","הנדסת חשמל"),
    ("5","הנדסה כימית")
)

YEAR_CHOICES = (
    ("1","שנה א"),
    ("2","שנה ב"),
    ("3","שנה ג"),
    ("4","שנה ד"),
)

SEMESTER_CHOICES = (
    ("1","סמסטר א"),
    ("2","סמסטר ב"),
    ("3","סמסטר קיץ"),
)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    permissions = models.BooleanField(default=True)
    imag_profile = models.ImageField(upload_to="images_profiles" , null=True, default='defProfile.png')


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100,null=True)
    Phone = PhoneNumberField()
    ID = models.CharField(max_length=10,null=True)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES, default='1')
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, default='1')
    semester = models.CharField(max_length=15, choices=SEMESTER_CHOICES, default='1')
    def __str__(self):
        return str(self.user.username)
   

class Lecturer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100,null=True)
    Phone = PhoneNumberField()
    ID = models.CharField(max_length=9,null=True)

    def __str__(self):
        return str(self.user.username)

