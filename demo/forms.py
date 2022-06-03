from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from .models import *
from ckeditor.widgets import CKEditorWidget

from .validators import is_even

class PostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['title', 'content', 'author', 'image_content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': CKEditorWidget(attrs={'class': 'form-control'}),
        }