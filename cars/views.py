import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Car
from .forms import CarForm


def home(request):
    return render(request,'base.html')

def car_list(request):
    return render(request, 'cars/car_list.html', {
        'cars': Car.objects.all(),
    })

def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "carListChanged": None,
                        "showMessage": f"{car.car_make} added."
                    })
                })
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {
        'form': form,
    })

def edit_car(request, pk):
    car = get_object_or_404(car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "carListChanged": None,
                        "showMessage": f"{car.car_make} updated."
                    })
                }
            )
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html.html', {
        'form': form,
        'car': car,
    })