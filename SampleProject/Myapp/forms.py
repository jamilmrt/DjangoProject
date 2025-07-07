from django import forms
from .models import Reservation  # Assuming Reservation model is defined in models.py

class ReservationForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields = '__all__'  # Include all fields from the Reservation model