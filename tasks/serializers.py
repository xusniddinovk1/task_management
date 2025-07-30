from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'assigned_to', 'status', 'priority', 'due_date', 'created_at',
                  'updated_at']
