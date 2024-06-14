from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/todos/", include("task_api.urls")),
    path("", include("todos_app.urls")),
]
