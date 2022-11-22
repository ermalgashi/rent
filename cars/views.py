import imp
from django.shortcuts import render
from .models import Car


def home(request):
    return render(request,'base.html')

def car_list(request):
    return render(request, 'cars/car_list.html', {
        'cars': Car.objects.all(),
    })