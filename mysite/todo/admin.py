from django.contrib import admin
from .models import Task, Userprofile

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'dueDate', 'status', 'user')
    list_filter = ('status', 'dueDate')

admin.site.register(Task, TaskAdmin)
admin.site.register(Userprofile)
