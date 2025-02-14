from django.shortcuts import render, redirect
from task.models import TaskModel

def home(request):
    tasks = TaskModel.objects.all()
    return render(request, 'home.html', {'tasks' : tasks})
