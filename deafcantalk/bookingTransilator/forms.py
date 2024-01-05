from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = ['client_name', 'client_email', 'start_time', 'end_time']