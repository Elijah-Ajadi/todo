from django.db import models
from django.contrib.auth.models import User
# from users.models import Profile

# Create your models here.
class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    TASK_TYPES_CHOICES = [
         ('normal', 'Normal'),
         ('important', 'Important'),
         ('super important', 'Super Important'),
    ]
    
    task_name = models.CharField(max_length=100,)
    task_description = models.TextField()
    task_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    task_type = models.CharField(max_length=50, choices=TASK_TYPES_CHOICES)
    task_status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='pending')
    
    
    def __str__(self):
        return self.task_name
    
    
    
class Category(models.Model):
    cat_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.cat_name