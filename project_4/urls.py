from django.contrib import admin
from django.urls import path, include
from therestaurant.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_homepage, name='get_homepage'),
    path('accounts/', include('allauth.urls')),
    path('reservetable/', reserve_table, name='reservetable'),
    path('viewbookings/', get_bookings, name='get_bookings'),
    path('menu/', get_menu, name='get_menu'),
    path('cancel_booking/<int:entry_id>/', cancel_booking, name='cancel_booking'),
    path('amend_booking/<int:entry_id>/', amend_booking, name='amend_booking'),
    path('reserve_success/', reserve_success, name='reserve_success')
]
