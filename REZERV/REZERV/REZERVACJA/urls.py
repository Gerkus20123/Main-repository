"""
URL configuration for REZERV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import path
from . import views

urlpatterns = [
    path('strona_glowna/', views.strona_glowna, name="strona_glowna"),
    path('lista_mieszkan/', views.lista_mieszkan, name="lista_mieszkan"),
    path('rezerwacja/', views.rezerwacja, name="rezerwacja"),
    path('rejestracja/', views.rejestracja, name="rejestracja"),
    path('o_nas/', views.o_nas, name="o_nas"),
    path('uslugi/', views.uslugi, name="uslugi"),
    path('zadaj_pytanie/', views.zadaj_pytanie, name="zadaj_pytanie"),
]
