from django.shortcuts import render
from .models import Klient, Meszkanie, Rezerwacja, Post
from .forms import FormularzKontaktowy, FormularzRejestracji, FormularzRezerwacji
import datetime
from django.http import HttpResponse

# Main page view
def strona_glowna(request):
    context = {"Post" : Post.objects.all()}
    return render(request, "Strona_Glowna.html", context)

# Registration page view
def rejestracja(request):
    if request.method == "POST":
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            pole_tekstowe = form.cleaned_data["pole_tekstowe"]
            return render(request, 'Rejestracja_sukces.html', {"pole_tekstowe": pole_tekstowe})
        else:
            return render(request, 'Rejestracja.html', {"form": form})
    else:
        form = FormularzRejestracji()
        return render(request, "Rejestracja.html", {"form": form})

# About Us page view
def o_nas(request):
    return render(request, "O nas.html")

# Our Services page view
def uslugi(request):
    return render(request, "Usługi.html")

# Apartment Offering page view
def lista_mieszkan(request):
    context = {"Mieszkanie" : Meszkanie.objects.all()}
    return render(request, "Oferta_Mieszkan.html", context)

# Ask a question page view
def zadaj_pytanie(request):
    if request.method == "POST":
        form = FormularzKontaktowy(request.POST)
        if form.is_valid():
            imie = form.cleaned_data["imie"]
            return render(request, 'Zadaj_pytanie_sukces.html', {"imie": imie})
        else:
            return render(request, 'Zadaj_pytanie.html', {"form": form})
    else:
        form = FormularzKontaktowy()
        return render(request, "Zadaj_pytanie.html", {"form": form})

# Make a reservation page view
def rezerwacja(request):
    if request.method == "POST":
        form = FormularzRezerwacji(request.POST)
        if form.is_valid():
            imie = form["imie"]
            return render(request, 'Rezerwacja_sukces.html', {"imie": imie})
        else:
            return render(request, 'Rezerwacja.html', {"form": form})
    else:
        form = FormularzRezerwacji()
        return render(request, "Rezerwacja.html", {"form": form})
