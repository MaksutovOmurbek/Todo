from django.urls import path
from apps.todo.views import *

urlpatterns = [
    path('todos/', ToDoAPIView.as_view(), name='todo-list'),
    path('todos/', DestroyAPIView.as_view(), name='todo-detail'),
    path('delete_user_todos/', CreateAPIView.as_view(), name='delete-user-todos'),
]
