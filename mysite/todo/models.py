from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
    task = models.CharField('Task', max_length=100, help_text='Task name')
    description = models.TextField('Description', max_length=1000, default="No comments.")
    insDate = models.DateTimeField('Instance date', auto_now_add=True)
    dueDate = models.DateField('Due date', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def is_overdue(self):
        if self.dueDate and date.today() > self.dueDate:
            return True
        return False

    def days_till_due(self):
        pass

    LOAN_STATUS = (
        ('c', 'Completed'),
        ('i', 'In progress'),
        ('u', 'Urgent'),
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
class Userprofile(models.Model):
    userProfile = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")
    def __str__(self):
        return f"{self.userProfile.username} profile"
