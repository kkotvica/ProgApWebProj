from django.shortcuts import render, get_object_or_404, redirect
from .models import Klient, Usługa, Pracownik, Rezerwacja
from .forms import KlientForm, UsługaForm, RezerwacjaForm, PracownikForm

# === Widoki Klienta ===
def klient_list(request):
    klienci = Klient.objects.all()
    return render(request, 'rezerwacje/klient_list.html', {'klienci': klienci})

def klient_detail(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    return render(request, 'rezerwacje/klient_detail.html', {'klient': klient})

def klient_edit(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = KlientForm(request.POST, instance=klient)
            if form.is_valid():
                form.save()
                return redirect('klient-detail-html', pk=klient.pk)
        elif 'delete' in request.POST:
            klient.delete()
            return redirect('klient-list-html')
    else:
        form = KlientForm(instance=klient)
    return render(request, 'rezerwacje/klient_edit.html', {'form': form, 'klient': klient})

def klient_add(request):
    if request.method == 'POST':
        form = KlientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('klient-list-html')
    else:
        form = KlientForm()
    return render(request, 'rezerwacje/klient_add.html', {'form': form})


# === Widoki Usługi ===
def usluga_list(request):
    uslugi = Usługa.objects.all()
    return render(request, 'rezerwacje/usluga_list.html', {'uslugi': uslugi})

def usluga_detail(request, pk):
    usluga = get_object_or_404(Usługa, pk=pk)
    return render(request, 'rezerwacje/usluga_detail.html', {'usluga': usluga})

def usluga_edit(request, pk):
    usluga = get_object_or_404(Usługa, pk=pk)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = UsługaForm(request.POST, instance=usluga)
            if form.is_valid():
                form.save()
                return redirect('usluga-detail-html', pk=usluga.pk)
        elif 'delete' in request.POST:
            usluga.delete()
            return redirect('usluga-list-html')
    else:
        form = UsługaForm(instance=usluga)
    return render(request, 'rezerwacje/usluga_edit.html', {'form': form, 'usluga': usluga})

def usluga_add(request):
    if request.method == 'POST':
        form = UsługaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usluga-list-html')
    else:
        form = UsługaForm()
    return render(request, 'rezerwacje/usluga_add.html', {'form': form})


# === Widoki Pracownika ===
def pracownik_list(request):
    pracownicy = Pracownik.objects.all()
    return render(request, 'rezerwacje/pracownik_list.html', {'pracownicy': pracownicy})

def pracownik_detail(request, pk):
    pracownik = get_object_or_404(Pracownik, pk=pk)
    return render(request, 'rezerwacje/pracownik_detail.html', {'pracownik': pracownik})

def pracownik_edit(request, pk):
    pracownik = get_object_or_404(Pracownik, pk=pk)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = PracownikForm(request.POST, instance=pracownik)
            if form.is_valid():
                form.save()
                return redirect('pracownik-detail-html', pk=pracownik.pk)
        elif 'delete' in request.POST:
            pracownik.delete()
            return redirect('pracownik-list-html')
    else:
        form = PracownikForm(instance=pracownik)
    return render(request, 'rezerwacje/pracownik_edit.html', {'form': form, 'pracownik': pracownik})

def pracownik_add(request):
    if request.method == 'POST':
        form = PracownikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pracownik-list-html')
    else:
        form = PracownikForm()
    return render(request, 'rezerwacje/pracownik_add.html', {'form': form})


# === Widoki Rezerwacji ===
def rezerwacja_list(request):
    rezerwacje = Rezerwacja.objects.all()
    return render(request, 'rezerwacje/rezerwacja_list.html', {'rezerwacje': rezerwacje})

def rezerwacja_detail(request, pk):
    rezerwacja = get_object_or_404(Rezerwacja, pk=pk)
    return render(request, 'rezerwacje/rezerwacja_detail.html', {'rezerwacja': rezerwacja})

def rezerwacja_edit(request, pk):
    rezerwacja = get_object_or_404(Rezerwacja, pk=pk)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = RezerwacjaForm(request.POST, instance=rezerwacja)
            if form.is_valid():
                form.save()
                return redirect('rezerwacja-detail-html', pk=rezerwacja.pk)
        elif 'delete' in request.POST:
            rezerwacja.delete()
            return redirect('rezerwacja-list-html')
    else:
        form = RezerwacjaForm(instance=rezerwacja)
    return render(request, 'rezerwacje/rezerwacja_edit.html', {'form': form, 'rezerwacja': rezerwacja})

def rezerwacja_add(request):
    if request.method == 'POST':
        form = RezerwacjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rezerwacja-list-html')
    else:
        form = RezerwacjaForm()
    return render(request, 'rezerwacje/rezerwacja_add.html', {'form': form})
