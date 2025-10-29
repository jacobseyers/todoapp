from django import forms

from .models import Todolist

#from .forms import TodolistForm

class TodolistForm(forms.Form):
    text = forms.CharField(max_length=200,
widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter a to-do item e.g Grocery Shopping', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
        )
    )
