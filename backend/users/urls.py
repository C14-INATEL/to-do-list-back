from django.urls import path
from .views import (
    CreateUserView,
    UserDetailView,
    NoteListCreateView,
    NoteDetailView,
    NoteDeletedListView,
    NoteRestoreView,
    ActivityLogView,
)

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='me'),

    path('notes/', NoteListCreateView.as_view(), name='notes'),
    path('notes/deleted/', NoteDeletedListView.as_view(), name='notes-deleted'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/<int:pk>/restore/', NoteRestoreView.as_view(), name='note-restore'),

    path('activity/', ActivityLogView.as_view(), name='activity'),
]
