from rest_framework.permissions import IsAuthenticated
from tasks.permissions import IsProjectMember
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectMember]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(members=user)
