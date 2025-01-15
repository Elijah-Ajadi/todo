from django.db import models
from tasks.models import Task
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    first_Name = models.CharField(max_length=50, null=True, blank=True)
    last_Name = models.CharField(max_length=60, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True)
    user_tasks = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return self.username
    
    
    
    
