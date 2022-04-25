from email.policy import default
from django import forms
from category.models import Course, HomeWork


class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ('department','year','semester','kind_of')

  def clean_kind_of(self):
    print("CHECK CHECK")
    kind_of = self.cleaned_data['kind_of']

    print(kind_of)
    if kind_of != "5":
      raise forms.ValidationError('Please Choice only YoTube')
    return kind_of


class CreatCourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ('department','year','semester','name_course','kind_of')
    widgers = {
      'name_course': forms.TextInput(attrs={ 'type':"text" ,'class':"bg-light form-control", }),
    }
    def clean_kind_of(self):
      print("CHECK CHECK")
      kind_of = self.cleaned_data['kind_of']

      print(kind_of)
      if kind_of != "5":
        raise forms.ValidationError('Please Choice only YoTube')
      return kind_of
