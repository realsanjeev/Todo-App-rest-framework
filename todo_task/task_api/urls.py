from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("auth/", obtain_auth_token),
    path("search/", views.todo_search_view),
    path("", views.todo_create_retrive_view),
    path("<int:pk>/", views.todo_detail_retrive_view, name="todo-detail"),
    path("<int:pk>/update", views.todo_update_view),
    path("<int:pk>/delete", views.todo_delete_view)
]
