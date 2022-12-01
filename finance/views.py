from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm


def check_car_availability(pickup_date, return_date, car):
   qs = Reservation.objects.filter(
      pickup_date__lte=pickup_date,
      return_date__gte=return_date,
      car = car,
      )

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



def reservations_add(request, **args):
   if request.method == "POST":
        form = ReservationForm(request.POST)

   else:
        form = ReservationForm()

   reservations = Reservation.objects.all()
   # reservations = Reservation.objects.filter(car=new_reservation.car)
   start_date = '2022-11-23'
   end_date = '2022-11-25'

   for reservation in reservations:
      print(check_car_availability(start_date, end_date, reservation.car))
   
   filter_params = dict(pickup_date__lte=end_date, return_date__gte=start_date) # just for redability
   is_occupied = Reservation.objects.filter(**filter_params, car__registration_number="01-603-KK")
  
   # for reservation in reservations:
   #    date_list = [reservation.pickup_date + datetime.timedelta(days=x) for x in range((reservation.return_date-reservation.pickup_date).days)]

   #    for date in date_list:
   #       print(date)
   
   return render(request, 'reservations/reservation_add.html', {
        'reservation': reservation, 'form': form,
    })
