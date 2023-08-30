from rest_framework import serializers
from task_api.models import TodoTask

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    class Meta:
        model = TodoTask
        fields = ["user", "task", "description", "completed", "timestamp", "updated"]
