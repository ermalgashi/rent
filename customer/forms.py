from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "name",
            "surname",
            "phone_number",
            "email",
            "license_id",
            "country",
        )
