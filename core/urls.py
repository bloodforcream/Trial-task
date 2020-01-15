from django.urls import path

from core.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, UserDetailAPIView, \
    TaskListAPIView, TaskCreateAPIView, TaskDeleteAPIView, TaskDetailAPIView, TaskUpdateAPIView, AssignedTasksAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('users/<int:pk>/edit/', UserUpdateAPIView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user_delete'),

    path('tasks/', TaskListAPIView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task_delete'),
    path('tasks/assigned-to/<int:pk>/', AssignedTasksAPIView.as_view(), name='assigned_task_list'),

]
