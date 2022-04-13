from dataclasses import fields
from django import forms
from HomePage.models import Post



class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','content')
