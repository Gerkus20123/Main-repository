from django import forms
from django.forms import PasswordInput
from django.utils import timezone

# Ask a question form
class FormularzKontaktowy(forms.Form):
    imie = forms.CharField(max_length=100, label="Imię")
    email = forms.EmailField(label="Email")
    wiadomosc = forms.CharField(widget=forms.Textarea, label="Wiadomość")

    # Name check
    def clean_imie(self):
        imie = self.cleaned_data['imie']
        if any(char.isdigit() for char in imie):
            raise forms.ValidationError("Imię nie może zawierać cyfr.")
        return imie

# Registration form
class FormularzRejestracji(forms.Form):
    pole_tekstowe = forms.CharField(max_length=50, label="Nazwa użytkownika")
    email = forms.EmailField(label="Adres email")
    haslo = forms.CharField(widget=PasswordInput, label="Hasło")
    potwierdz_haslo = forms.CharField(widget=PasswordInput, label="Potwierdź hasło")
    potwierdz_regulamin = forms.BooleanField(required=True, label="Akceptacja regulaminu")

    # password check
    def clean(self):
        cleaned_data = super().clean()
        haslo = cleaned_data.get("haslo")
        potwierdz_haslo = cleaned_data.get("potwierdz_haslo")

        if haslo and potwierdz_haslo and haslo != potwierdz_haslo:
            raise forms.ValidationError("Hasła muszą być identyczne.")

        return cleaned_data

# Reservation form
class FormularzRezerwacji(forms.Form):
    imie = forms.CharField(max_length=50, label="Imię")
    nazwisko = forms.CharField(max_length=50, label="Nazwisko")
    email = forms.EmailField(label="Adres e-mail")
    data_z = forms.DateTimeField(label="Data z")
    data_do = forms.DateTimeField(label="Data do")
    nr_mieszkania = forms.IntegerField(label="Numer mieszkania")