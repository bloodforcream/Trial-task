from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, null=True)


class Task(models.Model):
    name = models.CharField(max_length=200)
    reviewer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='review_tasks')
    assigned = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='assigned_tasks')
