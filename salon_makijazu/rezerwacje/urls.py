from django.urls import path
from . import views

urlpatterns = [
    path('klienci/', views.KlientList.as_view(), name='klient-list'),
    path('klienci/<int:pk>/', views.KlientDetail.as_view(), name='klient-detail'),
    path('uslugi/', views.UsługaList.as_view(), name='usluga-list'),
    path('uslugi/<int:pk>/', views.UsługaDetail.as_view(), name='usluga-detail'),
    path('pracownicy/', views.PracownikList.as_view(), name='pracownik-list'),
    path('pracownicy/<int:pk>/', views.PracownikDetail.as_view(), name='pracownik-detail'),
    path('rezerwacje/', views.RezerwacjaList.as_view(), name='rezerwacja-list'),
    path('rezerwacje/<int:pk>/', views.RezerwacjaDetail.as_view(), name='rezerwacja-detail'),
]
