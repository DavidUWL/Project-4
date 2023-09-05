from django.forms import ModelForm
from django import forms
from .models import Reservation


class ReserveForm(ModelForm):
    first_name = forms.TextInput(attrs={"required": True})
    last_name = forms.TextInput(attrs={"required": True})
    email = forms.EmailInput(attrs={"required": True})
    contact_number = forms.NumberInput(attrs={"required": True})

    date = forms.DateField(attrs={"required": True})
    time = forms.TimeField(attrs={"required": True})
    covers = forms.NumberInput(attrs={"required": True})

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email',
                  'contact_number', 'date', 'time', 'covers']
        widgets = {
            first_name: TextInput(attrs={"required": True}),
            last_name: TextInput(attrs={"required": True}),
            email: EmailInput(attrs={"required": True}),
            contact_number: NumberInput(attrs={"required": True}),

            date: DateField(attrs={"required": True}),
            time: TimeField(attrs={"required": True}),
            covers: NumberInput(attrs={"required": True})
        }