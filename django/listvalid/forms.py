from django.forms import ModelForm, TextInput
from django import forms
from .models import List

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['list']
        widgets = {'task': TextInput(attrs={
                'class': 'form-control',
                'name': 'list',
                'id': 'list',
                'placeholder': 'List'
            }),
            }