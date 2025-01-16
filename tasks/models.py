
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# from users.models import Profile

# Create your models here.
class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    
    task_name = models.CharField(max_length=100,)
    task_description = models.TextField()
    task_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    task_status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='pending')
    publish = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-publish',)
        
    
    def __str__(self):
        return self.task_name
    
    
    
class Category(models.Model):
    cat_name = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['cat_name']
    
    def __str__(self):
        return self.cat_name