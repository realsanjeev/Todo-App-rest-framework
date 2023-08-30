from rest_framework import serializers, validators
from task_api.models import TodoTask

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    description = serializers.CharField(source="desc", required=False)
    class Meta:
        model = TodoTask
        fields = ["user", "task", "description", "completed", "timestamp", "updated"]

    def validate_task(self, value):
        request = self.context.get("request")
        user = request.user
        if len(value) < 4:
            raise validators.ValidationError(f"task: `{value}`; length tooo short to take it as task")
        qs = TodoTask.objects.filter(user=user,
                                     title__iexact=value)
        if qs.exists():
            raise (f"Task with title: `{value}` already exists")
        return value