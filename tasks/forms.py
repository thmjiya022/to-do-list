from django import forms
from  django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete', 'due_date']
        widgets = {
                'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
