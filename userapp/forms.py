from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ('bookfor','date_from','date_to')

        widgets = {
            'date_from': forms.DateInput(attrs={'class': 'datepicker'}),
            'date_to': forms.DateInput(attrs={'class': 'datepicker'}),
        }



    # date_from = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    # date_to = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))