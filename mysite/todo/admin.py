from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'dueDate', 'status')

admin.site.register(Task, TaskAdmin)
