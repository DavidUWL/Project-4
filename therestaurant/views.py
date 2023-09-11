from django.shortcuts import render, redirect, reverse
from therestaurant.forms import ReserveForm
from .models import Reservation


# Create your views here.


def get_homepage(request):
    return render(request, 'home/home.html')


def get_reservation(request):
    return render(request, 'reservetable/reservetable.html')


def reserve_table(request):
    if request.POST:
        form = ReserveForm(request.POST)
        print(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
        return redirect('/reservetable')

    return render(request, 'reservetable/reservetable.html', {'form': ReserveForm})


def get_bookings(request):
    user_bookings = Reservation.objects.filter(user=request.user)
    return render(request, 'viewbooking/viewbookings.html', {'user_bookings': user_bookings})
