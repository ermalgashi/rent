from django.contrib import admin
from .models import Reservation

# Register your models here.

# admin.site.register(Reservation)


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "display_id",
        "customer",
        "car",
        "pickup_date",
        "return_date",
        "days",
        "price",
        "grand_total",
    )

    def display_id(self, instance):
        return f"Rezervimi {instance.id}"

    def days(self, instance):
        return instance.get_days()

    def grand_total(self, instance):
        return instance.grand_total()


admin.site.register(Reservation, ReservationAdmin)
