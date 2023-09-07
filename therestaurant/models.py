from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserProfile(models.model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact_number = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    covers = models.IntegerField(null=False, blank=False)