from django import forms
from .models import Kirim


class KirimForm(forms.ModelForm):
    class Meta:
        model = Kirim
        fields = ('title', 'destination', 'location', 'submission_date', 'arrival_date', 'price_in_RM', 'available_units_in_kg', 'description') 