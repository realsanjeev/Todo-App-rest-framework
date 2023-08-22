from django.urls import path
from task_api.views import TodoListAPIView, TodoDetailApi

urlpatterns = [
    path("api", TodoListAPIView.as_view(), name="api_view"),
    path("api/<int:todo_id>/", TodoDetailApi.as_view(), name="ai_task_detail"),
]
