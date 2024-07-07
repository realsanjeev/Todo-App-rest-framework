from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # template rendering path
    path("", include("myapp.urls")),
    path("admin/", admin.site.urls),
    # path used for django rest and its testing
    path("api/todos/", include("task_api.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema_docs",
    ),
]
