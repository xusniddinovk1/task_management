from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .filters import TaskFilter
from .permissions import IsTaskAssigneeOrProjectMember
from .serializers import TaskSerializer
from .models import Task
from rest_framework import filters


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskAssigneeOrProjectMember]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(project__members=user)

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Only admin can create tasks'}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            allowed_fields = {'status', 'priority'}
            if not set(request.data.keys()).issubset(allowed_fields):
                return Response({'detail': 'Faqat status va priority ni o‘zgartira olasiz.'},
                                status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Only admin can destroy projects'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
