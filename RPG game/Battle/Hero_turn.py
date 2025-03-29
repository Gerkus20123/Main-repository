
from Battle.Battle_functions_material import (enemies, enemy_HP, enemy_DF, classes, class_DF, class_AR, class_HP)

# Funkcja odpowiadająca za krok postaci w trakcie walki

def hero_turn(target, target_HP, target_DF, class_choice, DF, AR, HP, CT_hero):

# Battle variables
    Targ_name = enemies[target]
    Targ_HP = int(enemy_HP[target_HP])
    Targ_DF = int(enemy_DF[target_DF])
    Hero_AR = int(class_AR[AR])
    Hero_DF = int(class_DF[DF])
    Hero_HP = int(class_HP[HP])
    Hero_Class = classes[class_choice]
# Battle equations
    Hero_attack = Targ_DF - Hero_AR * CT_hero
    Targ_HP_afer_attack_hero = Targ_HP + Hero_attack
# Hero effects
    Hero_block_effect_on = int(Hero_DF + 2)
    Hero_prepares_effect_on = int(class_AR[AR]) + 3
    Hero_escapes = int(Hero_HP - 2)

# I. Hero choice
    question_action_choice = input("\nProszę wybrać swój krok: \n"
                        "1 - Atak\n"
                        "2 - Blokowanie (+2 DF w następnej turze)\n"
                        "3 - Przygotowanie się (+3 AR w następnej turze)\n"
                        "4 - Ucieczka\n")
# I.1. Hero choice - attack
    if question_action_choice == "1":
    # Target was attacked
        if Hero_attack < 0:
            print(Hero_Class.attack(Targ_name, str(Targ_HP_afer_attack_hero)))

            with open("../RPG game/txt_files/Target_HP.txt", 'w', encoding="UTF-8") as BL:
                BL.write(str(Targ_HP_afer_attack_hero))

    # Target evaded the attack
        if Targ_HP < Targ_HP_afer_attack_hero:
            print(Hero_Class.missed())
# I.2. Hero choice - block
    if question_action_choice == "2":
        Hero_blocks = Hero_Class.block(Targ_name, str(Hero_block_effect_on))
        print(Hero_blocks)

        with open("../RPG game/txt_files/Hero_DF.txt", 'w', encoding="UTF-8") as BL:
            BL.write(str(Hero_block_effect_on))

# I.3. Hero choice - prepares for the next attack
    if question_action_choice == "3":
        print(Hero_Class.prepare(str(Hero_prepares_effect_on)))

        with open("../RPG game/txt_files/Hero_AR.txt", 'w', encoding="UTF-8") as BL:
            BL.write(str(Hero_prepares_effect_on))

# I.4. Hero choice - escapes the battle
    if question_action_choice == "4":

        print(str(Hero_Class.escape()) + ". Tracisz 2 HP i 5 GL.")

        with open("../RPG game/txt_files/Hero_HP.txt", 'w', encoding="UTF-8") as BL:
            BL.write(str(Hero_escapes))

    return Targ_HP_afer_attack_hero, Hero_block_effect_on, Hero_prepares_effect_on, Hero_escapes

