from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, CategoryForm


def index(request):
    return render(request, "welcome.html")

def completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.task_status = 'completed'
    task.save()
    
    return redirect('dashboard')
def dashboard(request):
    
    todos = Task.objects.exclude(task_status = 'completed')
    
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('dashboard')
        
    elif request.method == 'POST':
        catform = CategoryForm(request.POST)
        if catform.is_valid():
            catform.save()
        
        return redirect('dashboard')
    
    else:
        catform = CategoryForm()
        form = TaskForm()
        
    context = {
        'form': form,
        'catform': catform,
        'todos': todos,
        
    }
    
    return render(request, "dashboard.html", context)
