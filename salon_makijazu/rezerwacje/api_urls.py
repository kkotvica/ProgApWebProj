from django.urls import path
from . import api_views

urlpatterns = [
    path('klienci/', api_views.KlientList.as_view(), name='klient-list-api'),
    path('klienci/<int:pk>/', api_views.KlientDetail.as_view(), name='klient-detail-api'),
    path('uslugi/', api_views.UsługaList.as_view(), name='usluga-list-api'),
    path('uslugi/<int:pk>/', api_views.UsługaDetail.as_view(), name='usluga-detail-api'),
    path('pracownicy/', api_views.PracownikList.as_view(), name='pracownik-list-api'),
    path('pracownicy/<int:pk>/', api_views.PracownikDetail.as_view(), name='pracownik-detail-api'),
    path('rezerwacje/', api_views.RezerwacjaList.as_view(), name='rezerwacja-list-api'),
    path('rezerwacje/<int:pk>/', api_views.RezerwacjaDetail.as_view(), name='rezerwacja-detail-api'),
    path('rezerwacje/klient/<int:klient_id>/', api_views.RezerwacjeKlienta.as_view(), name='rezerwacje-klienta-api'),
    path('uslugi/cena/<int:min_cena>/<int:max_cena>/', api_views.UslugiWPrzedzialeCenowym.as_view(),name='uslugi-przedzial-cenowy-api'),
]
