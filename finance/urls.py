from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.reservations_base , name='reservations_base'),
    path('reservations_add', views.reservations_add , name='reservations_add'),
    path('reservations_list/', views.reservations_list , name='reservations_list'),
    path('reservations_detail/<int:pk>/', views.reservations_detail , name='reservations_detail'),
    
]