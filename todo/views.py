from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    #solo le paso task ya que el resto de los campos son automaticos
    Task.objects.create(task=task)
    return redirect('home')
