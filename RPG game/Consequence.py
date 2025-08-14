from Encounters.Items import Item_list
from Encounters.Shop import Shop_list
from Class_files.Chosen_class_read import read_class
from Battle.battle import battle_system
from locations.Create_random_map_function import move
from Encounters.monsters.Enemies import enemy_encountered_list_name, enemy_encountered_list_letter
from Encounters.Hero_gold_total import hero_GL_T, Hero_GL_T_calc

import random

# Funkcja tworząca akcji z przypadkami w zależności od klatki, na której nasza postać się znajduje
def consequence(move_done, map):
    move_consequence = move(map, move_done)

    if (move_consequence == "O" or move_consequence == "T"
            or move_consequence == "R" or move_consequence == "W" or move_consequence == "G"):
        print("\nNapotkałeś/aś przeciwnika: " + enemy_encountered_list_name(move_consequence) + "\n")
        battle_system(enemy_encountered_list_letter(move_consequence), read_class())

    if move_consequence == "Item":
        it = random.choice(Item_list)
        print("\nZnalazłeś/aś przedmiot: " + str(it["ID"]) + ".")

    if move_consequence == "GL":
        gold_obtained = str(random.choice([i for i in range(1,250)]))
        print("\nZnalazłeś/aś " + gold_obtained + " złota.\n")

        with open("../RPG game/txt_files/Hero_gold_obtained.txt", 'w', encoding="UTF-8") as f:
            f.write(gold_obtained)
            f.close()
            total_gold = Hero_GL_T_calc(int(hero_GL_T()), int(gold_obtained)) - int(hero_GL_T())
        print("Masz: " + str(total_gold) + " GL.")

    if move_consequence == "Empty":
        print("\nKlatka jest pusta.\n")

    if move_consequence == "Merchant":
        print("Znalazłeś/aś wędrownego handlarza.")

        question_if_buy = input("Czy chcesz coś kupić? (1 - Tak, 2 - Nie)\n")
        if question_if_buy == "1":
            it_1 = Shop_list[0]
            it_2 = Shop_list[1]
            print("Handlarz ma następujące przedmioty:\n "
                    "1) " + str(it_1["ID"]) + ": " + str(it_1["Gold cost"]) + " gold\n"
                    "2) " + str(it_2["ID"]) + ": " + str(it_2["Gold cost"]) + " gold\n")
            question_to_buy = input("Wybierz przedmiot do kupowania (od 1 do 10): ")
            if question_to_buy == "1":
                print("Kupiłeś: " + it_1["ID"])
            if question_to_buy == "2":
                print("Kupiłeś: " + it_2["ID"])