from django.utils import timezone
from django import forms
from django.db import models
from .models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'task_category',]
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']