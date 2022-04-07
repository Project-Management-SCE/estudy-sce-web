
from django import forms
from accounts.models import StudentUser


class NewStudentForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    verifyPass = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = StudentUser
        fields = '__all__'
