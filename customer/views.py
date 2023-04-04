import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import CustomerForm
from .models import Customer
from django.core.paginator import Paginator

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


# Create your views here.
def customer_base(request):
    customers = Customer.objects.all().order_by("-id")
    p = Paginator(customers, 5)
    page_number = request.GET.get("page")
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {"page_obj": page_obj}

    return render(request, "customer/customer_base.html", context)


def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)

    return render(
        request,
        "customer/customer_detail.html",
        {
            "customer": customer,
        },
    )


def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            if "customers" in request.META.get("HTTP_REFERER"):
                return HttpResponse(
                    status=204,
                    headers={
                        "HX-Trigger": json.dumps(
                            {
                                "customerListChanged": None,
                                "showMessage": f"{customer.name} added.",
                            }
                        )
                    },
                )
            else:
                return HttpResponseRedirect("/reservations_add/")
    else:
        form = CustomerForm()
    return render(
        request,
        "customer/customer_form.html",
        {
            "form": form,
        },
    )


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "customerListChanged": None,
                            "showMessage": f"{customer.name} updated.",
                        }
                    )
                },
            )
        
    else:
        form = CustomerForm(instance=customer)
    return render(
        request,
        "customer/customer_form.html",
        {
            "form": form,
            "customer": customer,
        },
    )
