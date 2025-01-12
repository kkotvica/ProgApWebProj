from django.urls import path
from .views import (
    klient_list, klient_detail, klient_edit, klient_add,
    usluga_list, usluga_detail, usluga_edit, usluga_add,
    pracownik_list, pracownik_detail, pracownik_edit, pracownik_add,
    rezerwacja_list, rezerwacja_detail, rezerwacja_edit, rezerwacja_add,dashboard
)

urlpatterns = [
    # Klienci
    path('klienci/', klient_list, name='klient-list-html'),
    path('klienci/add/', klient_add, name='klient-add-html'),
    path('klienci/<int:pk>/', klient_detail, name='klient-detail-html'),
    path('klienci/<int:pk>/edit/', klient_edit, name='klient-edit-html'),

    # Usługi
    path('uslugi/', usluga_list, name='usluga-list-html'),
    path('uslugi/add/', usluga_add, name='usluga-add-html'),
    path('uslugi/<int:pk>/', usluga_detail, name='usluga-detail-html'),
    path('uslugi/<int:pk>/edit/', usluga_edit, name='usluga-edit-html'),

    # Pracownicy
    path('pracownicy/', pracownik_list, name='pracownik-list-html'),
    path('pracownicy/add/', pracownik_add, name='pracownik-add-html'),
    path('pracownicy/<int:pk>/', pracownik_detail, name='pracownik-detail-html'),
    path('pracownicy/<int:pk>/edit/', pracownik_edit, name='pracownik-edit-html'),

    # Rezerwacje
    path('rezerwacje/', rezerwacja_list, name='rezerwacja-list-html'),
    path('rezerwacje/add/', rezerwacja_add, name='rezerwacja-add-html'),
    path('rezerwacje/<int:pk>/', rezerwacja_detail, name='rezerwacja-detail-html'),
    path('rezerwacje/<int:pk>/edit/', rezerwacja_edit, name='rezerwacja-edit-html'),

    path('dashboard/', dashboard, name='dashboard'),
]