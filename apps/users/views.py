from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.users.models import Todo, User
from Todo.apps.users.serializers import TodoSerializers, UserSerializers

class UserAPIView(CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


