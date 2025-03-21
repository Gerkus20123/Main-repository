# from locations.cave import
# from locations.city import
# from locations.forest import

# from characters.warrior import Warrior
# from characters.mage import Mage
# from characters.archer import Archer

import random

def RPG():
    while True:
        print("Witaj w grze RPG")
        zapytanie_1 = input("Wybierz mapę, na której bedziesz grał: 1 - Dungeon, 2 - Forest, 3 - City:\n ")
        if zapytanie_1 == "1":
            lista_1 = [i for i in range(1,400)]
            print(random.choice(lista_1))
        if zapytanie_1 == "2":
            lista_2 = [i for i in range(1,300)]
            print(random.choice(lista_2))
        if zapytanie_1 == "3":
            lista_3 = [i for i in range(1,2500)]
            print(random.choice(lista_3))
        print("W tej grze są trzy klasy:\n "
              "1) Warrior: Zdrowie (HF) 25, punkty obrarzeń (AR) 5, obrona (DF) 10"
              "2) Mage: Zdrowie (HF) 15, punkty obrarzeń (AR) 3, obrona (DF) 4, mana (MN) 15"
              "3) Archer: Zdrowie (HF) 20, punkty obrarzeń (AR) 4, obrona (DF) 6")
        zapytanie_2 = input("Wybierz klasę, za którą chesz grać: (wpisz cyfrę od 1 do 3):\n")
        if zapytanie_2 == "1":
            print("20x20 = 400")
        if zapytanie_2 == "2":
            print("30x10 = 300")
        if zapytanie_2 == "3":
            print("50x50 = 2500")
        print("Koniec gry!!!")
        break

RPG()