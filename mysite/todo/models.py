from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
    task = models.CharField('Task', max_length=100, help_text='Task name')
    description = models.TextField('Description', max_length=1000)
    insDate = models.DateTimeField('Instance date', auto_now_add=True)
    dueDate = models.DateField('Due date', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.dueDate and date.today() > self.dueDate:
            return True
        return False

    LOAN_STATUS = (
        ('u', 'Urgent'),
        ('c', 'Completed'),
        ('i', 'In progress'),
        ('n', 'Need extra time'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='i',
        help_text='Status',
    )
    class Meta:
        ordering = ['dueDate']
    def __str__(self):
        return f'{self.task} | Due: {self.dueDate}'
