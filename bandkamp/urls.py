from django.contrib import admin
from django.urls import include, path
from drf_spectacular import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("albums.urls")),
    path("schema/", views.SpectacularApiView.as_view(), name="schema"),
    path("api/docs/", views.SpectacularSwaggerView.as_view(url_name="schema")),
]
