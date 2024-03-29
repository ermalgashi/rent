from django.db import models


FUEL_TYPE_CHOICES = (
    ("DIESEL", "Diesel"),
    ("PETROL", "Petrol"),
    ("ELECTRIC", "Electric"),
    ("PROPANE", "Propane"),
)

INSURANCE = (
    ("CASCO/REGIONAL", "Casco/Regional"),
    ("BASIC/REGIONAL", "Basic/Regional"),
    ("CASCO/LOCAL", "Casco/Local"),
    ("BASIC/LOCAL", "Basic/Local"),
)


# Create your models here.
class Car(models.Model):
    car_make = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_year = models.CharField(max_length=10)
    car_engine = models.CharField(max_length=10)
    car_fuel_type = models.CharField(
        max_length=10, choices=FUEL_TYPE_CHOICES, default="DIESEL"
    )
    car_value = models.IntegerField()
    car_capacity = models.IntegerField()
    registration_number = models.CharField(max_length=20, unique=True)
    registration_date = models.DateField()
    registration_expiration_date = models.DateField()
    insurance_type = models.CharField(max_length=20, choices=INSURANCE, default="BASIC")
    vin = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    referal_price = models.DecimalField(max_digits=5, decimal_places=2)
    # In the future Owner should have own table, to be linked with foreignkey
    # Later we need to add status field where it needs to have
    # choices such as (in_rent, available, in_service, ...)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.registration_number}"

    def get_referal_price(self):
        return self.referal_price
