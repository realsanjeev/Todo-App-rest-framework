from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class TodoTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.task
