from django.shortcuts import render
from .models import Reservation
from cars.models import Car
import datetime

# Create your views here.
def reservations_base(request):
   return render(request,'reservations/reservation_base.html')

def reservations_list(request):
   reservations = Reservation.objects.all()
   start_date = '2022-11-24'
   end_date = '2022-11-26'
   filter_params = dict(pickup_date__lte=end_date, return_date__gte=start_date) # just for redability
   is_occupied = Reservation.objects.filter(**filter_params, car__registration_number="01-603-KK").exists()
   
   # Code to test from stackoverflow.
   # for date in date_list: 
   # ...:     start_date, end_date = date.values() 
   # ...:     filter_params = dict(booked_for_datetime__date__lte=end_date, booked_till_datetime__date__gte=start_date) 
   # ...:     is_occupied = Booking.objects.filter(**filter_params, room__name=101).exists() 
   # ...:     if is_occupied: 
   # ...:         print('Not Available on this range, start: {} end: {}'.format(start_date, end_date)) 
   # ...:     else: 
   # ...:         print('Available on this range, start: {} end: {}'.format(start_date, end_date)) 


   return render(request,'reservations/reservation_list.html', {'reservations' : reservations })

def reservations_detail(request, pk):
    reservation = Reservation.objects.get(pk=pk)

    return render(request, 'reservations/reservation_detail.html', {
        'reservation': reservation,
    })