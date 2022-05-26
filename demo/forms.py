from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['title', 'content', 'author', 'image_content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }