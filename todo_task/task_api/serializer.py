from rest_framework import serializers
from task_api.models import TodoTask

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ["task", "user", "completed", "timestamp", "updated"]
