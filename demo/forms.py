import imp
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['title', 'content', 'author', 'image_content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorWidget(attrs={'class': 'form-control'}),
        }