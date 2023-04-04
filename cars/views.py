import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Car
from .forms import CarForm
from django.core.paginator import Paginator


def home(request):
    cars = Car.objects.all().order_by("registration_expiration_date")

    p = Paginator(cars, 10)
    page_number = request.GET.get("page")
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {"page_obj": page_obj}

    return render(request, "cars/car_base.html", context)


def detail_car(request, pk):
    car = Car.objects.get(pk=pk)

    return render(
        request,
        "cars/car_detail.html",
        {
            "car": car,
        },
    )


def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "carListChanged": None,
                            "showMessage": f"{car.car_make} added.",
                        }
                    )
                },
            )
    else:
        form = CarForm()
    return render(
        request,
        "cars/car_form.html",
        {
            "form": form,
        },
    )


def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "carListChanged": None,
                            "showMessage": f"{car.car_make} updated.",
                        }
                    )
                },
            )
    else:
        form = CarForm(instance=car)
    return render(
        request,
        "cars/car_form.html",
        {
            "form": form,
            "car": car,
        },
    )
