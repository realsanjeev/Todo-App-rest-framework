from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# defining the namespace
app_name = "todos"
urlpatterns = [
    path("", views.GenericListView.as_view(), name="index"),
    path(
        "completed-task/", views.CompletedTaskListView.as_view(), name="completed-task"
    ),
    path("<int:todo_id>/delete", views.delete, name="delete-task"),
    path("<int:todo_id>/update", views.update, name="update-task"),
    path("add/", views.add, name="add-task"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
