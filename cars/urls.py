from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='cars'),
    path('cars', views.car_list, name='car_list'),
    path('cars/add_car', views.add_car, name='add_car'),
    path('cars/<int:pk>/edit', views.edit_car, name='edit_car'),
]
