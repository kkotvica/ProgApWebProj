
from .models import Klient, Usługa, Pracownik, Rezerwacja
from django.shortcuts import render,get_object_or_404, redirect


def klient_list(request):
    klienci = Klient.objects.all()
    return render(request, 'rezerwacje/klient_list.html', {'klienci': klienci})

def klient_detail(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    return render(request, 'rezerwacje/klient_detail.html', {'klient': klient})

def usluga_list(request):
    uslugi = Usługa.objects.all()
    return render(request, 'rezerwacje/usluga_list.html', {'uslugi': uslugi})

def usluga_detail(request, pk):
    usluga = get_object_or_404(Usługa, pk=pk)
    return render(request, 'rezerwacje/usluga_detail.html', {'usluga': usluga})

def pracownik_list(request):
    pracownicy = Pracownik.objects.all()
    return render(request, 'rezerwacje/pracownik_list.html', {'pracownicy': pracownicy})

def rezerwacja_list(request):
    rezerwacje = Rezerwacja.objects.all()
    return render(request, 'rezerwacje/rezerwacja_list.html', {'rezerwacje': rezerwacje})
