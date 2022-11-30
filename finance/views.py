from django.shortcuts import render
from .models import Reservation
from cars.models import Car
import datetime as dt
import datetime

def check_car_availability(pickup_date, return_date, car):
   qs = Reservation.objects.filter(
      pickup_date__lte=pickup_date,
      return_date__gte=return_date,
      car = car,
      )

   #  if len(qs) >= room_count:
   #      return False
   return True




# Create your views here.
def reservations_base(request):
   return render(request,'reservations/reservation_base.html')

def reservations_list(request):
   reservations = Reservation.objects.all()   
   return render(request,'reservations/reservation_list.html', {'reservations' : reservations})

def reservations_detail(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    return render(request, 'reservations/reservation_detail.html', {
        'reservation': reservation,
    })



def reservations_add(request):
   new_reservation = Reservation.objects.get()
   reservations = Reservation.objects.filter(car__registration_number=new_reservation.car)
   start_date = '2022-11-10'
   end_date = '2022-11-13'

   check_car_availability(start_date, end_date, "01-603-KK")
   
   filter_params = dict(pickup_date__lte=end_date, return_date__gte=start_date) # just for redability
   is_occupied = Reservation.objects.filter(**filter_params, car__registration_number="01-603-KK")
  
   for reservation in reservations:
      date_list = [reservation.pickup_date + datetime.timedelta(days=x) for x in range((reservation.return_date-reservation.pickup_date).days)]

      for date in date_list:
         print(date)
   
   #  new_reservation = Reservation.objects.get(pk=1)
   
   # reservations = Reservation.objects.filter(car__registration_number=new_reservation.car)
   # start_date = '2022-11-20'
   # end_date = '2022-11-30'
   # filter_params = dict(pickup_date__lte=end_date, return_date__gte=start_date) # just for redability
   # is_occupied = Reservation.objects.filter(**filter_params, car__registration_number="01-603-KK")
  
   # for reservation in reservations:
   #    date_list = [reservation.pickup_date + datetime.timedelta(days=x) for x in range((reservation.return_date-reservation.pickup_date).days)]

   #    for date in date_list:
   #       print(date)
   
   # date_list = [ 
   #    dict(start=start_date, end=end_date), 
   # ]

  
   # base = dt.datetime.strptime(reservation.pickup_date, "%Y-%m-%d")
   # end_base = dt.datetime.strptime(reservation.return_date, "%Y-%m-%d")     

   # # Code to test from stackoverflow.
   # for date in date_list: 
   #      start_date, end_date = date.values() 
   #      filter_params = dict(pickup_date__lte=end_date, return_date__gte=start_date)
   #      is_occupied = Reservation.objects.filter(**filter_params, car__registration_number="01-603-KK").exists() 
   #      if is_occupied: 
   #          print('Not Available on this range, start: {} end: {}'.format(start_date, end_date)) 
   #      else: 
   #          print('Available on this range, start: {} end: {}'.format(start_date, end_date)) 

   return render(request, 'reservations/reservation_add.html', {
        'reservation': reservation,
    })
