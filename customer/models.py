from django.db import models

COUNTRIES = (
    ("ALBANIA", 'Albania'),
    ("KOSOVO", 'Kosovo'),
    ('ITALY', 'Italy'),
    ('USA', 'Usa'), 
    #we will add others when we need, 
    # or maybe create a new table for coutries, if needed
)

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    license_id = models.CharField(max_length=50)
    country = models.CharField(max_length=10, choices= COUNTRIES, default='ITALY')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name} {self.surname}'
