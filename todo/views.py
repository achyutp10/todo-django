from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Task

# Create your views here.

def addTask(request):
  if request.method == 'POST':
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
