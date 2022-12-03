from django.http import HttpResponse
from django.db import models
from django.urls import reverse

COUNTRIES = (
    ("ALBANIA", "Albania"),
    ("KOSOVO", "Kosovo"),
    ("ITALY", "Italy"),
    ("USA", "Usa"),
    # we will add others when we need,
    # or maybe create a new table for coutries, if needed
)

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    license_id = models.CharField(max_length=50, unique=True)
    # Adding Scanned License should be optional, but will it help the data or is it not nescessary.
    country = models.CharField(max_length=10, choices=COUNTRIES, default="ITALY")
    # Maybe we should add customer rating, to help us decide whether should we keep serving him or no!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_url(self):
        return HttpResponse("Succesfully Added Customer")
