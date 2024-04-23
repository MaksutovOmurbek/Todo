from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.users.models import  User
from apps.users.serializers import  UserSerializers

class UserAPIViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin
                     ):
    queryset = User.objects.all()
    serializer_class = UserSerializers



