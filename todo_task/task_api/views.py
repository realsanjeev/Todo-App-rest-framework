from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from task_api.models import TodoTask
from task_api.serializer import TodoSerializer

# Create your views here.
class TodoListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        todos = TodoTask.objects.filter(user=request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "user": request.user.id,
            "task": request.data.get("task"),
            "completed": request.data.get("completed")
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id, user_id):
        try:
            return TodoTask.objects.get(id=todo_id, user=user_id)
        except TodoTask.DoesNotExist:
            return None

    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id=todo_id, user_id=request.user.id)
        if not todo_instance:
            return Response(
                {"res": f"Task with id :{todo_id} doesnot exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TodoSerializer(todo_instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id=todo_id, user_id=request.user.id)
        if not todo_instance:
            return Response(
                {"res": f"Todo Task with id: {todo_id} doesnot exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        data = {
            "user": request.user.id,
            "task": request.data.get("task"),
            "completed": request.data.get("completed")
        }
        serializer = TodoSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id=todo_id, user_id=request.user.id)
        if not todo_instance:
            return Response(
                {"res": f"Todo Task of id: {todo_id} doesnot exist"}
            )
        todo_instance.delete()
        return Response(
            {"res": "Todo Task Sucessfully deleted!!!"},
            status=status.HTTP_204_NO_CONTENT
        )