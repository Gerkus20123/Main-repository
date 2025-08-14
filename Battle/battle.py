from Cube_Throw.Cube_throw_for_battle_hero import CT_hero
from Cube_Throw.Cube_throw_for_battle_enemy import CT_enemy

from Battle.Hero_turn import hero_turn
from Battle.Enemy_turn import enemy_turn

# Funkcja odpowiadająca za proces walki

def battle_system(enemy_encountered, hero_class):
    while True:
        Cube_throw_hero_question = input("\nKliknij dowolny klawisz by rzucić kostkę.\n")

        Hero = CT_hero()

        Enemy = CT_enemy()

        if Hero > Enemy:
            hero_turn(enemy_encountered, enemy_encountered, enemy_encountered, hero_class, hero_class, hero_class, hero_class, Hero)
            with open("../RPG game/txt_files/Target_HP.txt", 'r', encoding="utf-8") as enemy_HP_after_attack:
                for i in enemy_HP_after_attack:
                    if int(i) <= 0:
                        enemy_HP_after_attack.read()
                        print("\nPokonałeś przeciwnika.\n")
                        break
                    if int(i) > 0:
                        battle_system(enemy_encountered, hero_class)
        if Enemy > Hero:
            enemy_turn(enemy_encountered, enemy_encountered, hero_class, hero_class, Enemy)
            with open("../RPG game/txt_files/Hero_HP.txt", 'r', encoding="utf-8") as hero_HP_after_attack:
                for i in hero_HP_after_attack:
                    hero_HP_after_attack.read()
                    if int(i) <= 0:
                        print("\nJesteś pokonany.\n")
                        break
            with open("../RPG game/txt_files/Hero_HP.txt", 'r', encoding="utf-8") as hero_HP_after_attack:
                for i in hero_HP_after_attack:
                    hero_HP_after_attack.read()
                    if int(i) > 0:
                        battle_system(enemy_encountered, hero_class)
        if Enemy == Hero:
            print("\nWyniki kostek są podobne.\n")
            continue
        return