from .models import Task
from django import forms
from django.contrib.auth.models import User
class DateInput(forms.DateInput):
    input_type = 'date'
class UserTaskCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description', 'dueDate', 'status']
        widgets = {'user': forms.HiddenInput(), 'dueDate': DateInput()}