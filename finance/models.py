from django.db import models
from customer.models import Customer
from cars.models import Car
from django.contrib.auth.models import User

FUEL_CAPACITY = (
    ("1/4", "1/4"),
    ("2/4", "2/4"),
    ("3/4", "3/4"),
    ("4/4", "4/4"),
)

EXPENSES_TYPES = (
    ("Terheqje", "TERHEQJE"),
    ("Servis", "SERVIS"),
    ("Reprezentacion", "REPREZENTACION"),
    ("Tjeter", "TJETER"),
)

PAYMENT = (
    ("Cash", "Kesh"),
    ("Card","Kartelë"),
)


# Create your models here.
class Reservation(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    fuel_capacity = models.CharField(max_length=10, choices=FUEL_CAPACITY)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pickup_date = models.DateField()
    return_date = models.DateField()
    payment = models.CharField(max_length=10, choices=PAYMENT)

    def get_days(self):
        return (self.return_date - self.pickup_date).days

    def get_pickup_date(self):
        return self.pickup_date

    def grand_total(self):
        # duhet qartesohet data e fillimit dhe e kthimit.
        return ((self.return_date - self.pickup_date).days+1) * self.price

    def check_avialability(self):
        return self.pickup_date - self.return_date
        # We need a function that connects with the reservation app to check if the car is available on given dates

    def customer_revenue(self):
        pass

    def car_revenue(self):
        pass


class Expenses(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=15, choices=EXPENSES_TYPES)
    expense_sum = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.expense_type} - {self.comments}"