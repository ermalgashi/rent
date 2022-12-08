import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse

from .models import Reservation
from .forms import ReservationForm


def check_car_availability(pickup_date, return_date, car):
    qs = Reservation.objects.filter(car=car)
    avaliable_list = []
    for reservation in qs:
        if (
            pickup_date > reservation.return_date
            or return_date < reservation.pickup_date
        ):
            avaliable_list.append(True)
        else:
            avaliable_list.append(False)
 
    return all(avaliable_list)


# Create your views here.
def reservations_base(request):
    return render(request, "reservations/reservation_base.html")


def reservations_list(request):
    reservations = Reservation.objects.all().order_by("pickup_date")
    return render(
        request, "reservations/reservation_list.html", {"reservations": reservations}
    )


def reservations_detail(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    return render(
        request,
        "reservations/reservation_detail.html",
        {
            "reservation": reservation,
        },
    )


def reservations_add(request):
    reservations = Reservation.objects.all().order_by("-return_date")
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if check_car_availability(
                data["pickup_date"], data["return_date"], data["car"]
            ):
                form.save()
                return HttpResponse(
                    status=204,
                    headers={
                        "HX-Trigger": json.dumps(
                            {
                                "reservationListChanged": None,
                            }
                        )
                    },
                )
            else:
               form = ReservationForm(request.POST)
    else:
        form = ReservationForm()

    return render(
        request,
        "reservations/reservation_add.html",
        {
            "reservation": reservations,
            "form": form,
        },
    )
