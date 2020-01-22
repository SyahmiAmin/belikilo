from django.db import models

# Create your models here.


class Kirim(models.Model):

    # title
    title = models.CharField(max_length=120)

    # destination
    CAIRO_TO_KL = 'CAI-KUL'
    KL_TO_CAIRO = 'KUL-CAI'
    KIRIM_DESTINATION_CHOICES = [
        (CAIRO_TO_KL, 'Cairo to KL'),
        (KL_TO_CAIRO, 'KL to Cairo'),
    ]
    destination = models.CharField(max_length=10, choices=KIRIM_DESTINATION_CHOICES, default=CAIRO_TO_KL)

    # location
    location = models.CharField(max_length=120)


    # last submission date
    submission_date = models.DateField(auto_now=False, auto_now_add=False)
    # expected arrival date 
    arrival_date = models.DateField(auto_now=False, auto_now_add=False)
    
    # price per kg
    price_in_RM = models.DecimalField(decimal_places=2, max_digits=4, default=20.00)

    # available units (kg)
    available_units_in_kg = models.IntegerField(default=1)

    # description
    description     = models.TextField(blank=True)

    def __str__(self):
        return self.title