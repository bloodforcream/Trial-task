from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from core.serializers import UserSerializer, UserCreateSerializer, TaskCreateSerializer, TaskSerializer
from core.models import User, Task


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ['role']

    def get_queryset(self):
        with_task = self.request.GET.get('with_task')
        if with_task:
            queryset = User.objects.filter(assigned_tasks__assigned__isnull=False)
        else:
            queryset = User.objects.all()
        return queryset


class AssignedTasksAPIView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            queryset = Task.objects.filter(assigned=pk)
        else:
            queryset = User.objects.all()

        return queryset


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [SearchFilter]
    search_fields = ['name']


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
