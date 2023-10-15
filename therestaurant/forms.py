from django.forms import ModelForm
from django import forms
from .models import Reservation


class ReserveForm(ModelForm):
    COVERS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

    TIME_CHOICES = [
        (1700, '17:00'),
        (1800, '18:00'),
        (1900, '19:00'),
        (2000, '20:00'),
        (2100, '21:00'),
        (2200, '22:00'),
    ]

    covers = forms.ChoiceField(
        choices=COVERS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True}),
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
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', "required": True}),
            'time': forms.TimeInput(attrs={'type': 'btn', 'class': 'form-control', "required": True}),
            # 'covers': forms.Select(attrs={'class': 'form-control'}),
        }

