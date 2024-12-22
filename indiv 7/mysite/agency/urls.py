from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("agency/<int:agency_id>/", views.detail, name="detail"),

    path("edit_agency/<int:agency_id>/", views.edit_agency, name="edit_agency"),

    path('add_agency/', views.add_agency, name='add_agency'),
]