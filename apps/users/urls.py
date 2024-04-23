from django.urls import path
from apps.users.views import *

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user-list'),
    path('users/', UserAPIView.as_view(), name='user-detail'),
    path('todos/', TodoAPIView.as_view(), name='todo-list'),
    path('todos/', TodoDetailAPIView.as_view(), name='todo-detail'),
    path('delete_user_todos/', TodoCreateAPIView.as_view(), name='delete-user-todos'),
]
