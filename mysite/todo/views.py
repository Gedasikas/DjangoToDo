from .models import Task
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    context_object_name = 'tasks'
    template_name = 'tasks.html'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'


