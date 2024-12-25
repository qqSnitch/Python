from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("agency/<int:agency_id>/", views.agency_detail, name="agency_detail"),

    path("employee/<int:employee_id>/", views.employee_detail, name="employee_detail"),

    path("contract/<int:contract_id>/", views.contract_detail, name="contract_detail"),

    path("edit_agency/<int:agency_id>/", views.edit_agency, name="edit_agency"),

    path('add_agency/', views.add_agency, name='add_agency'),
]