from django.shortcuts import render, redirect, reverse, get_object_or_404
from therestaurant.forms import ReserveForm
from .models import Reservation, Table, Menu
from datetime import *

def get_homepage(request):
    return render(request, 'home/home.html')


def get_reservation(request):
    return render(request, 'reservetable/reservetable.html', {'user': request.user})


def get_available_table(selected_date, selected_time, covers):
    available_tables = Table.objects.filter(table_covers__gte=covers)
    
    for table in available_tables:
        if not Reservation.objects.filter(table=table, date=selected_date, time=selected_time).exists():
            return table

    return None  # No available table found


# Allows user to make a reservation 
def reserve_table(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            
            selected_date = form.cleaned_data['date']
            selected_time = form.cleaned_data['time']
            covers = form.cleaned_data['covers']
   
            selected_table = get_available_table(selected_date, selected_time, covers)

            if selected_table:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.table = selected_table
                reservation.save()

                return redirect('reservetable')
            else:
                error_message = "No available tables for the selected time and ddcovers."
                return render(request, 'reservetable', {'form': form, 'error_message': error_message})
    else:
        form = ReserveForm()

    return render(request, 'reservetable/reservetable.html', {'form': form})


# Where user views their own bookings when authenticated
def get_bookings(request):
    user_bookings = Reservation.objects.filter(user=request.user)
    today = date.today() 
    return render(request, 'viewbooking/viewbookings.html', {'user_bookings': user_bookings, 'today': today})


def get_menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})


def cancel_booking(request, entry_id):
    entry = get_object_or_404(Reservation, pk=entry_id)

    if request.method == 'POST':
        if form.is_valid():
            entry.delete()
            return redirect('get_bookings')
    return render(request, 'cancel_booking/cancel_booking.html', {'entry': entry})


def amend_booking(request, entry_id):
    entry = get_object_or_404(Reservation, pk=entry_id)

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=entry)
        form.save()
        return redirect('get_bookings')

    else:
        form = ReserveForm(instance=entry)

    return render(request, 'amend_booking/amend_booking.html', {'form': form})

