from django.forms import ModelForm
from django import forms
from .models import Reservation


class ReserveForm(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailInput()
    contact_number = forms.NumberInput()

    date = forms.DateField()
    time = forms.TimeField()
    covers = forms.NumberInput()

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email',
                  'contact_number', 'date', 'time', 'covers']
