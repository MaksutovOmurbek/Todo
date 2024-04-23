from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.users.models import Todo, CustomUser
from apps.serializers import TodoSerializers, UserSerializers

class UserAPIView(CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers


class TodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class TodoDetailAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

# CreateAPIView for creating a new Todo
class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class TodoCreateAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


# Create your views here.
