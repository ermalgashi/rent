from django.db import models
from customer.models import Customer
from cars.models import Car

# Create your models here.
class Reservation(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    pickup_date = models.DateField()
    return_date = models.DateField()

    
    def get_days(self):
        return (self.return_date - self.pickup_date ).days
    
    def grand_total(self):
        # duhet qartesohet data e fillimit dhe e kthimit.
        return str((self.return_date - self.pickup_date ).days  * self.price) + " $"