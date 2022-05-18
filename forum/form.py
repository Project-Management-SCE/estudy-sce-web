import django

from django import forms
from forum.models import Post, Comment


class PostForumForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("message",)
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "placeholder": "What's on your mind, Estudy?",
                    "spellcheck": "false",
                    "style": "width: 449px; height: 120px;",
                }
            )
        }
