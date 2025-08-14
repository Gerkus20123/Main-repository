# To jest główny plik gry


from Class_files.Chosen_class_write import write_class
from locations.Write_map_chosen import write_chosen_map as map_write
from locations.Read_map_chosen import RM
from locations.Create_random_map_function import create_map
from Movement import movement_2


def Game():
    while True:
# Punkt I. Powitanie

        print("\n///////// Witaj w grze RPG 'Nighty Nights'. /////////\n")

# Punkt II. Dokumentacja gry

        question_readme = input("Czy chcesz zobaczyć dokumentację gry? \n(Proszę wpisać 'Tak', "
                                "albo kliknąć na dowolny klawisz jeśli nie):\n ")

        if question_readme == "Tak" or question_readme == "tak":
            with open("Readme.txt", encoding="utf-8") as file:
                print(file.read())

# Punkt III. Wybór mapy

        question_map_choice = input("\nWybierz mapę, na której będziesz grał:\n"
                                    "1 - Loch (15 klatek, gra jest najszybsza)\n"
                                    "2 - Las (50 klatek, średni czas grania)\n"
                                    "3 - Miasto (100 klatek, gra jest najdłuższa)\n")
        map_write(question_map_choice)
        create_map(question_map_choice)

# Punkt IV. Wybór klasy
        print("""\nMasz trzy klasy na wybór:\n
1) Wojownik: Zdrowie (HP) 25, punkty obrażeń (AR) 5, obrona (DF) 10\n
2) Mag: Zdrowie (HP) 15, punkty obrażeń (AR) 3, obrona (DF) 4, mana (MN) 15,
Dostępne zaklęcia: 
- Fireball (8 AR, -4 MN), 
- Blessing (+5 HP, -5 MN)\n
3) Łucznik: Zdrowie (HP) 20, punkty obrażeń (AR) 4, obrona (DF) 6\n""")

        question_hero_class_choice = input("Wybierz klasę, za którą chcesz grać: "
                                           "1 - Wojownik, "
                                           "2 - Mag, "
                                           "3 - Łucznik\n")

        write_class(question_hero_class_choice)

# Punkt V. Gra
        movement_2(RM(), create_map(question_map_choice))
# Punkt VI. Pożegnanie
        print("Koniec gry!!!")

        with open("../RPG game/txt_files/Map_chosen.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Chosen_class.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Hero_AR.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Hero_DF.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Hero_HP.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Hero_MN.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Map_chosen.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Target_HP.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        with open("../RPG game/txt_files/Hero_gold_obtained.txt", 'w', encoding="utf-8") as MC:
            MC.write("")
            MC.close()
        break

Game()

