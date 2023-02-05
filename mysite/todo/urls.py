from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task'),
    path('register/', views.register, name='register'),
    path('tasks/new', views.TaskByUserCreateView.as_view(), name='user_task_form'),
]