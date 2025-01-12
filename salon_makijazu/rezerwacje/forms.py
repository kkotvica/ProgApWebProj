from django import forms
from .models import Klient, Usługa, Pracownik, Rezerwacja

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = '__all__'

class UsługaForm(forms.ModelForm):
    class Meta:
        model = Usługa
        fields = '__all__'

class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        fields = '__all__'

class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = '__all__'