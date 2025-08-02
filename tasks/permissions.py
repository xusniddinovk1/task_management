from rest_framework import permissions
from tasks.models import Task


class IsTaskAssigneeOrProjectMember(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Allows for admins
        if request.user.is_staff:
            return True
        # Allow only for task member
        if obj.assigned_to == request.user:
            return True

        if request.user in obj.project.members.all():
            return True
        return False


class IsProjectMember(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user in obj.members.all()


class IsTaskProjectMemberOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if request.method == 'POST':
            task_id = request.data.get('task')
            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                return False
            return request.user in task.project.members.all()
        return True
