from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("", views.home, name="cars"),
    path("cars/<int:pk>/detail", views.detail_car, name="detail_car"),
    path("cars/add_car", views.add_car, name="add_car"),
    path("cars/<int:pk>/edit", views.edit_car, name="edit_car"),
]
