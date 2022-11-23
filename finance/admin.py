from django.contrib import admin
from .models import Reservation
from cars.models import Car
# Register your models here.

# admin.site.register(Reservation)

class ReservationAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',), }
    list_display = ('display_id','customer', 'car', 
                    'pickup_date', 'return_date','days','price' ,'grand_total')
    
    def display_id(self, instance):
        return f'Rezervimi {instance.id}'
    
    def days(self, instance):
        return instance.get_days()

    def grand_total(self, instance):
        return instance.grand_total()
    
    # def referal_price(self, instance):
    #     car = objects.get
    #     return instance.get_referal_price()


admin.site.register(Reservation, ReservationAdmin)