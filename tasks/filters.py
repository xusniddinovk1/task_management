from django_filters import rest_framework as django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'priority': ['exact'],
            'project': ['exact'],
            'assigned_to': ['exact'],
        }
