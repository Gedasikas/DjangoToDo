from django.db import models

class Task(models.Model):
    task = models.CharField('Task', max_length=100, help_text='Task name')
    description = models.TextField('Description', max_length=1000)
    insDate = models.DateTimeField('Instance date', auto_now_add=True)
    dueDate = models.DateField('Due date', blank=True, null=True)

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
    def __str__(self):
        return f'{self.task} | Due: {self.dueDate}'
