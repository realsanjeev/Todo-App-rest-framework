from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from task_api.models import TodoTask


class GenericListView(generic.ListView):
    template_name = "todos/index.html"
    context_object_name = "todo_list"

    def get_queryset(self) -> QuerySet[Any]:
        return TodoTask.objects.order_by("updated")


def add(request, *args, **kwargs):
    task = request.POST.get("task")
    desc = request.POST.get("desc")
    if desc is None:
        desc = task

    TodoTask.objects.create(task=task, desc=desc)
    return redirect("todos:index")


def delete(request, *args, **kwargs):
    id = kwargs.get("todo_id")
    todo = get_object_or_404(TodoTask, pk=id)

    todo.delete()
    return redirect("todos:index")


def update(request, *args, **kwargs):
    id = kwargs.get("todo_id")
    completed = request.POST.get("completed", False)
    if completed == "on":
        completed = True
    todo = get_object_or_404(TodoTask, pk=id)

    todo.completed = completed
    todo.save()
    return redirect("todos:index")
