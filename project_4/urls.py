"""project_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('cancel_booking/<int:entry_id>/', cancel_booking, name='cancel_booking')
]

