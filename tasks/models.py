from django.db import models
from projects.models import Project
from users.models import CustomUser

STATUS = (
    ('TODO', 'todo'),
    ('IN_PROGRESS', 'in_progress'),
    ('REVIEW', 'review'),
    ('DONE', 'done')
)

PRIORITY_CHOICES = [
    ('LOW', 'low'),
    ('MEDIUM', 'medium'),
    ('HIGH', 'high')
]


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=11, choices=STATUS, default='TODO')
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='MEDIUM')
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
