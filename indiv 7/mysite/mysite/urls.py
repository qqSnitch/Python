from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("agency.urls")),
    path("edit_agency/", include("agency.urls")),
    path("admin/", admin.site.urls),
]