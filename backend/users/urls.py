from django.urls import path
from .views import CreateUserView
from .views import UserDetailView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='me'),
]