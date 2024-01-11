from django.contrib import admin
from .models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('bookfor','tenant','date_from','date_to')


admin.site.register(Booking,BookingAdmin)