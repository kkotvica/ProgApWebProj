from rest_framework import serializers
from .models import Klient, Usługa, Pracownik, Rezerwacja

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'

class UsługaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usługa
        fields = '__all__'

class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'

class RezerwacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezerwacja
        fields = '__all__'
