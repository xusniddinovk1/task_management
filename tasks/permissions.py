from rest_framework import permissions


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
