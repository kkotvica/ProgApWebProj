from django.urls import path
from . import views

urlpatterns = [
    path('klienci/', views.klient_list, name='klient-list-html'),
    path('klienci/<int:pk>/', views.klient_detail, name='klient-detail-html'),
    path('uslugi/', views.usluga_list, name='usluga-list-html'),
    path('uslugi/<int:pk>/', views.usluga_detail, name='usluga-detail-html'),
    path('pracownicy/', views.pracownik_list, name='pracownik-list-html'),
    path('rezerwacje/', views.rezerwacja_list, name='rezerwacja-list-html'),
]