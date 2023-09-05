from django.shortcuts import render, redirect, reverse
from therestaurant.forms import ReserveForm


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
            form.save()
        return redirect('/reservetable')
    return render(request, 'reservetable/reservetable.html', {'form': ReserveForm})

