from django_filters import rest_framework as django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    priority = django_filters.CharFilter(field_name='priority', lookup_expr='exact')
    project = django_filters.NumberFilter(field_name='project__id', lookup_expr='exact')
    assigned_to = django_filters.NumberFilter(field_name='assigned_to__id', lookup_expr='exact')

    class Meta:
        model = Task
        fields = ['status', 'priority', 'project', 'assigned_to']