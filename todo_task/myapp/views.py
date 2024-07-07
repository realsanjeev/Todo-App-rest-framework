from typing import Any

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from task_api.models import TodoTask

from .forms import LoginForm, SignUpForm


class GenericListView(generic.ListView):
    template_name = "todos/index.html"
    context_object_name = "todo_list"

    def get_queryset(self) -> QuerySet[Any]:
        return TodoTask.objects.order_by("updated")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "account/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


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
