from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['customer', 'car', 'price', 'pickup_date', 'return_date']