from django.urls import path
from .views import CreateUserView
from .views import UserDetailView
from .views import NoteListCreateView
from .views import NoteDetailView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='me'),

    path('notes/', NoteListCreateView.as_view(), name='notes'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]