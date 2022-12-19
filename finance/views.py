import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os

from .models import Reservation
from .forms import ReservationForm

from customer.models import Customer

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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
    reservations = Reservation.objects.all().order_by("-id")
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


def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "carListChanged": None,
                            "showMessage": f"{reservation.car_make} updated.",
                        }
                    )
                },
            )
    else:
        form = ReservationForm(instance=reservation)
    return render(
        request,
        "reservations/reservation_form.html",
        {
            "form": form,
            "reservation": reservation,
        },
    )

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL     # Typically /static/
    #static Root
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, link_callback=link_callback)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


def print_invoice(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    customer = Customer.objects.get(pk=reservation.customer.pk)
    data = {
        "address": customer.country,
        "phone": customer.phone_number,
        "name": customer.name,
        "surname": customer.surname,
        "email": customer.email,
        "license_id": customer.license_id,
        "grand_total": reservation.grand_total(),
        "car": reservation.car,
        "days": reservation.get_days(),
        "price": reservation.price,

    }

    pdf = render_to_pdf('reservations/pdf_template.html', data)


    return HttpResponse(pdf, content_type='application/pdf')
