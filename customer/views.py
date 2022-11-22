from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from customer.forms import CustomerForm
from .models import Customer

# Create your views here.
def add_customer(request, id=None):
    form = CustomerForm()
    # form = CustomerForm(request.POST or None, request.FILES or None, instance=instance) 
    # kjo eshte mundesi edit/permirsime
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # return HttpResponseRedirect(instance.get_url())
            return HttpResponse("Sucessfully Added customer")

    return render(request, 'customer/add_customer.html', {'form':form})
