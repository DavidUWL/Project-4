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
        (17.00, '17.00'),
        (17.30, '17.30'),
        (18.00, '18.00'),
        (18.30, '18.30'),
        (19.00, '19.00'),
        (19.30, '19.30'),
        (20.00, '20.00'),
        (20.30, '20.30'),
        (21.00, '21.00'),
        (21.30, '21.30'),
        (22.00, '22.00'),
        (22.30, '22.30'),
        (23.00, '23.00'),
    ]

    covers = forms.ChoiceField(
        choices=COVERS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'required': True}),
    )

    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'required': True}),
    )

    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'email',
                  'contact_number', 'date', 'time', 'covers']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', "required": True}),
            'contact_number': forms.NumberInput(attrs={'type': 'tel', 'class': 'form-control', "required": True}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', "required": True}),
            # 'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', "required": True}),
            # 'covers': forms.Select(attrs={'class': 'form-control'}),
        }

