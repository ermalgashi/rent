from django.shortcuts import render
from .models import Car

# Create your views here.
def home(request):
    cars = Car.objects.all()
    return render(request, 'cars/base.html', {'cars':cars})