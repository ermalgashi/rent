import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import CustomerForm
from .models import Customer

# Create your views here.
def customer_base(request):
    customers = Customer.objects.all()
    return render(request,'customer/customer_base.html', {"customers":customers})

def customer_list(request):
    
    return render(request, 'customer/customer_list.html', {
        'customers': Customer.objects.all().order_by("-id"),
    })

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    
    return render(request, 'customer/customer_detail.html', {
        'customer': customer,
    })


def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "customerListChanged": None,
                        "showMessage": f"{customer.name} added."
                    })
                })
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_form.html', {
        'form': form,
    })


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "customerListChanged": None,
                        "showMessage": f"{customer.name} updated."
                    })
                }
            )
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer_form.html', {
        'form': form,
        'customer': customer,
    })
