from django.contrib import admin
from .models import Reservation
from .models import Menu


@admin.register(Reservation)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class PersonAdmin(admin.ModelAdmin):
    pass

