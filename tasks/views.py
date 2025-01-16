from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Task


def index(request):
    return render(request, "welcome.html")

def completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.task_status = 'completed'
    task.save()
    
def dashboard(request):
    return render(request, "dashboard.html")
