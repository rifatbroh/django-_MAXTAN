from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import TaskModel


def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            return redirect('add_task')
    return render(request, 'task/add_task.html', {'form' : form})


def edit_task(request, id):
    tsk = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=tsk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tsk)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task/add_task.html', {'form' : form})

def delete_task(request, id):
    TaskModel.objects.get(pk=id).delete()
    return redirect('home')


def mark_completed(request, id):
    tsk = TaskModel.objects.get(pk=id)
    tsk.completed = True
    tsk.save()
    return redirect('home')