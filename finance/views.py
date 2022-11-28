from django.shortcuts import render
from .models import Reservation

# Create your views here.
def reservations_base(request):
   return render(request,'reservations/reservation_base.html')

def reservations_list(request):
   return render(request,'reservations/reservation_list.html')