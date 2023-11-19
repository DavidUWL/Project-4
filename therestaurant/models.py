from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.forms.widgets import DateInput


class Table(models.Model):
    table_number = (models.IntegerField(unique=True))
    table_covers = (models.IntegerField())

    def __str__(self):
        return f"Table {self.table_number}" 


def get_default_table():
    try:
        return Table.objects.get(table_number=1)
    except Table.DoesNotExist:
        return None


class ReturnFutureDates(DateInput):
    def __init__(self, attrs=None):
        super().__init__(attrs={'min': date.today().strftime('%Y-%m-%d'), **(attrs or {})})


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact_number = models.CharField(max_length=15, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    covers = models.IntegerField(null=False, blank=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=get_default_table)

    def __str__(self):
        return f"{self.date} | {self.time} | {self.table}" 


class Menu(models.Model):
    dish_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=80, null=True, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')

    def __str__(self):
        return self.dish_name