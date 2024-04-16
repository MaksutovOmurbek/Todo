from rest_framework import serializers
from apps.base.models import CustomUser, Todo

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number']

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'description', 'created_at', 'updated_at']
