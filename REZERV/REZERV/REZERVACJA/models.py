from django.db import models
from django.db.models import IntegerField
from django.utils import timezone

# Model tworzący tabelę z danymi klienta
class Klient(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

# Model tworzący tabelę z danymi o mieszkaniu
class Meszkanie(models.Model):
    Nr_mieszkania = IntegerField(default=0)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    miasto = models.CharField(max_length=200)
    adres = models.CharField(max_length=500)
    liczba_osob = models.IntegerField(default=1)
    powierzchnia = models.IntegerField(default=1)
    liczba_pokojow = models.IntegerField(default=1)
    opis = models.CharField(max_length=500)
    dostepnosc = models.BooleanField(default=False)
    data_publikowania = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"Numer Mieszkania: {self.Nr_mieszkania}\n"
                f"Cena: {self.cena}\n"
                f"Miasto: {self.miasto}\n"
                f"Adres: {self.adres}\n"
                f"Liczba osób: {self.liczba_osob}\n"
                f"Powierzchnia: {self.powierzchnia}\n"
                f"Liczba pokojów: {self.liczba_pokojow}\n"
                f"Opis mieszkania: {self.opis}\n"
                f"Czy dostępne: {self.dostepnosc}\n"
                f"Data publikowania: {self.data_publikowania}\n")


# Model tworzący tabelę z danymi o rezerwacjach
class Rezerwacja(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    meszkanie = models.ForeignKey(Meszkanie, on_delete=models.CASCADE)
    data_utworzenia = models.DateTimeField(default=timezone.now)
    data_z = models.DateTimeField(default=timezone.now)
    data_do = models.DateTimeField(default=timezone.now)


# Model tworzący tabelę z danymi o postach na stronie głównej
class Post(models.Model):
    Nr_post = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    opis = models.CharField(max_length=1000)
    data_publikowania = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (f"Numer postu: {self.Nr_post}\n"
                f"Tytuł: {self.title}\n"
                f"Opis: {self.opis}\n"
                f"Data publikowania: {self.data_publikowania}\n")