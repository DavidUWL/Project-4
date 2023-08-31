from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact_number = models.IntegerField(null=False, blank=False)


class Booking(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_id = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    covers = models.IntegerField(null=False, blank=False)