from django.db import models

class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField()
    telefon = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Usługa(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nazwa

class Pracownik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    specjalizacja = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.specjalizacja}"

class Rezerwacja(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    usługa = models.ForeignKey(Usługa, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return f"Rezerwacja {self.usługa} dla {self.klient} na {self.data}"
