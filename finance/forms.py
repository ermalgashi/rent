import datetime
from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["customer", "car", "price", "pickup_date", "return_date"]

    def clean_pickup_date(self, *args, **kwargs):
        pickup_date = self.cleaned_data.get("pickup_date")
        car = self.cleaned_data.get("car")

        reservations = Reservation.objects.filter(car=car)

        for reservation in reservations:
           date_list = [reservation.pickup_date + datetime.timedelta(days=x) for x in range((reservation.return_date-reservation.pickup_date).days)]

        # for date in date_list:
        #     print(date)

        if pickup_date in date_list:
            raise forms.ValidationError("Kjo date per kete veture eshte e rezervuar")
        else:
            return pickup_date

        # date_list = [ 
        #    dict(start=start_date, end=end_date), 
        # ]


        # base = dt.datetime.strptime(reservation.pickup_date, "%Y-%m-%d")
        # end_base = dt.datetime.strptime(reservation.return_date, "%Y-%m-%d")     

        # # Code to test from stackoverflow.
        # for date in date_list: 
        #      start_date, end_date = date.values() 
        #      filter_params = dict(pickup_date__lte=end_date, return_date__gte=start_date)
        #      is_occupied = Reservation.objects.filter(**filter_params, car__registration_number="01-603-KK").exists() 
        #      if is_occupied: 
        #          print('Not Available on this range, start: {} end: {}'.format(start_date, end_date)) 
        #      else: 
        #          print('Available on this range, start: {} end: {}'.format(start_date, end_date)) 

        