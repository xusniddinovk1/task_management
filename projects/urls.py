from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from tasks.views import TaskViewSet
from comments.views import CommentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
