from django.shortcuts import render
from rest_framework import status, permissions, generics, authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from task_api.models import TodoTask
from task_api.serializer import TodoSerializer

class TodoCreateListAPIView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class TodoUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoSerializer

class TodoDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoSerializer

todo_create_retrive_view = TodoCreateListAPIView.as_view()
todo_update_view = TodoUpdateAPIView.as_view()
todo_delete_view = TodoDeleteAPIView.as_view()