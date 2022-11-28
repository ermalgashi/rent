from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.reservations_base , name='reservations_base'),
    path('reservations_list/', views.reservations_list , name='reservations_list'),

]