from django import forms

from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['car_make', 'car_model', 'car_year', 'car_engine', 'car_fuel_type', 
            'car_capacity', 'registration_number', 'registration_date', 'registration_expiration_date',
            'insurance_type', 'vin', 'color', 'owner']