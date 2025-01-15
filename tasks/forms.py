from django.utils import timezone
from django import forms
from django.db import models
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'task_category', 'task_type']