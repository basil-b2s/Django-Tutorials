from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def addTask(request):
    # print(request.POST)
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect("home")

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')
