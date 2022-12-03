from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path("", views.customer_base, name="customer_base"),
    path("customer_detail/<int:pk>", views.customer_detail, name="customer_detail"),
    path("customer_list/", views.customer_list, name="customer_list"),
    path("customer_add/", views.customer_add, name="customer_add"),
    path("customer_edit/<int:pk>", views.customer_edit, name="customer_edit"),
]
