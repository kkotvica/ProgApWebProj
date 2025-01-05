from rest_framework import generics
from .models import Klient, Usługa, Pracownik, Rezerwacja
from .serializers import KlientSerializer, UsługaSerializer, PracownikSerializer, RezerwacjaSerializer

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class UsługaList(generics.ListCreateAPIView):
    queryset = Usługa.objects.all()
    serializer_class = UsługaSerializer

class UsługaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usługa.objects.all()
    serializer_class = UsługaSerializer

class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer

class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer

class RezerwacjaList(generics.ListCreateAPIView):
    queryset = Rezerwacja.objects.all()
    serializer_class = RezerwacjaSerializer

class RezerwacjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rezerwacja.objects.all()
    serializer_class = RezerwacjaSerializer
