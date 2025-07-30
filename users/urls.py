from django.urls import path
from .views.register import RegisterView
from .views.login import LoginVIew

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginVIew.as_view(), name='login'),
]
