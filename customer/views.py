from django.shortcuts import render, redirect

from customer.forms import CustomerForm
from .models import Customer

# Create your views here.
def add_customer(request, id=None):

    # form = CustomerForm(request.POST or None, request.FILES or None, instance=instance) 
    # kjo eshte mundesi edit/permirsime
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # return HttpResponseRedirect(instance.get_url())
            return redirect('/')
    else:
        form = CustomerForm()

    return render(request, 'customer/add_customer.html', {'form':form})
