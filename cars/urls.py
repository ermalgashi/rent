from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='cars'),
    path('cars', views.car_list, name='car_list'),
]