from django.shortcuts import render
from rest_framework import status, permissions, generics, authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from task_api.models import TodoTask
from task_api.serializer import TodoSerializer
from task_api.authentication import TokenAutentication

class TodoCreateListAPIView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication, TokenAutentication]
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        task = serializer.validated_data.get("task")
        desc = serializer.validated_data.get("description")
        if desc is None:
            desc = task
        serializer.save(user=self.request.user, desc=desc)

class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = TodoTask.objects.all()
    lookup_field = "pk"
    serializer_class = TodoSerializer

class TodoUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        task = serializer.validated_data.get("task")
        desc = serializer.validated_data.get("description")
        if desc is None:
            desc = task
        serializer.save(user=self.request.user, desc=desc)

class TodoDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoSerializer

todo_create_retrive_view = TodoCreateListAPIView.as_view()
todo_detail_retrive_view = TodoDetailAPIView.as_view()
todo_update_view = TodoUpdateAPIView.as_view()
todo_delete_view = TodoDeleteAPIView.as_view()

