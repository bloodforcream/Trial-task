from rest_framework.serializers import ModelSerializer

from core.models import User, Task


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'role',
        ]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'role',
        ]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'reviewer',
            'assigned'
        ]


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'reviewer',
            'assigned'
        ]