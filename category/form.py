from django import forms
from category.models import Course, HomeWork



class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ('department','year','semester','kind_of')


class HomeWorkForm(forms.ModelForm):
  class Meta:
    model = HomeWork
    fields = ('nameFile','file','course')