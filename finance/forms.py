import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["customer", "car", "price", "pickup_date", "return_date", "fuel_capacity"]

    def clean(self, *args, **kwargs):
        pickup_date = self.cleaned_data.get("pickup_date")
        return_date = self.cleaned_data.get("return_date")
        car = self.cleaned_data.get("car")

        reservations = Reservation.objects.filter(car=car)
        
        
        date_list = []
        booked_dates = [pickup_date + datetime.timedelta(days=x) for x in range((return_date-pickup_date).days)]
        
        
        for reservation in reservations:
           date_list += [reservation.pickup_date + datetime.timedelta(days=x) for x in range((reservation.return_date-reservation.pickup_date).days)]
           
        if return_date < pickup_date:
            raise ValidationError("Data e kthimit nuk duhet te jete me e vogel se data e marrjes")

        if pickup_date in date_list:
            raise ValidationError("Kjo date marrje për këtë veturë është e rezervuar")

        if return_date in date_list:
            raise ValidationError("Kjo date kthimi për këtë veturë është e rezervuar")
        
        for date in booked_dates:
            if date in date_list:
                raise ValidationError(f"Data me afert lire per kthim te kesaj veture eshte {min(date_list)}")
        
