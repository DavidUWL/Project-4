from django.forms import ModelForm
from django import forms
from .models import Reservation
from django.forms.widgets import DateInput
from datetime import date

class ReturnFutureDates(DateInput):
    def __init__(self, attrs=None):
        super().__init__(attrs={'min': date.today().strftime('%Y-%m-%d'), **(attrs or {})})


class ReserveForm(ModelForm):
    COVERS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

    TIME_CHOICES = [
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
        ('22:00', '22:00'),
    ]

    covers = forms.ChoiceField(
        choices=COVERS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            }),
    )

    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    class Meta:
        model = Reservation
        fields = ['first_name','last_name','email',
                  'contact_number', 'date', 'time', 'covers']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', "required": True}),
            'contact_number': forms.NumberInput(attrs={'type': 'tel', 'class': 'form-control', "required": True}),
            'date': ReturnFutureDates(attrs={'type': 'date', 'class': 'form-control', "required": True}),
        }

