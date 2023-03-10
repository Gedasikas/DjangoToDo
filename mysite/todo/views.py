from django.urls import reverse
from .models import Task
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,)
from .forms import UserTaskCreateUpdateForm
from django.contrib.auth.decorators import login_required

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
class TaskByUserCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = UserTaskCreateUpdateForm
    success_url = '/todo/'
    template_name = 'user_task_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class TaskByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    form_class = UserTaskCreateUpdateForm
    template_name = 'user_task_form.html'

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.object.id})
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user

class TaskByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    success_url = '/todo/'
    template_name = 'user_task_delete.html'
    context_object_name = 'delete_task'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reik??mes i?? registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slapta??od??iai
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} u??imtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. pa??tu {email} jau u??registruotas!')
                    return redirect('register')
                else:

                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} u??registruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slapta??od??iai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def userprofile(request):
    return render(request, 'userprofile.html')





