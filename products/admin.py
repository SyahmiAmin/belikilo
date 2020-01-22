from django.contrib import admin

# Register your models here.
from .models import Kirim

class KirimAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'destination', 
        'location', 
        'submission_date', 
        'arrival_date', 
        'price_in_RM', 
        'available_units_in_kg', 
        'description',
    )
    
admin.site.register(Kirim, KirimAdmin)