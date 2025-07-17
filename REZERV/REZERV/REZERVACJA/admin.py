from django.contrib import admin
from .models import Klient, Meszkanie, Rezerwacja, Post

class KlientAdmin(admin.ModelAdmin):
    list_display = ("imie",
                    "nazwisko",
                    "telefon",
                    "email")

    list_filter = ("imie",
                   "nazwisko")

    search_fields = ("imie",
                     "nazwisko")

class MeszkanieAdmin(admin.ModelAdmin):
    list_display = ("Nr_mieszkania",
                    "cena",
                    "miasto",
                    "adres",
                    "liczba_osob",
                    "powierzchnia",
                    "liczba_pokojow",
                    "opis",
                    "dostepnosc")

    search_fields = ("dostepnosc",
                     "miasto",
                     "liczba_osob")

class RezerwacjaAdmin(admin.ModelAdmin):
    list_display = ("klient",
                    "meszkanie",
                    'data_utworzenia',
                    'data_z',
                    'data_do')

    search_fields = ("klient", )

class PostAdmin(admin.ModelAdmin):
    list_display = ("Nr_post",
                    "title",
                    "opis",
                    "data_publikowania")

    search_fields = ("Nr_post",
                     "title",
                     "data_publikowania", )

admin.site.register(Klient, KlientAdmin)
admin.site.register(Meszkanie, MeszkanieAdmin)
admin.site.register(Rezerwacja, RezerwacjaAdmin)
admin.site.register(Post, PostAdmin)

