from django.contrib import admin
from .models import Student , Lecturer, User

admin.site.register(User)
admin.site.register(Lecturer)
admin.site.register(Student)
