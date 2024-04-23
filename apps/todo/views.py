from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.todo.models import ToDo
from apps.todo.serializers import ToDoSerializer

class ToDoAPIView(ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset =ToDo.objects.all()
    serializer_class =ToDoSerializer

# Create your views here.
