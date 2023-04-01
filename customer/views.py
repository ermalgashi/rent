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

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')






# Create your views here.
def customer_base(request):
    customers = Customer.objects.all()
    p = Paginator(customers, 2)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html

    return render(request, "customer/customer_base.html", context)


def customer_list(request):
    return render(
        request,
        "customer/customer_list.html",
        {
            "customers": Customer.objects.all().order_by("-id"),
        },
    )


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
