from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views import generic

class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    context_object_name = 'tasks'
    template_name = 'tasks.html'

class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'


