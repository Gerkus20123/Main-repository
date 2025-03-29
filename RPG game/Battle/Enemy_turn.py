from Battle.Battle_functions_material import (enemies_upper, enemy_AR, class_DF, class_HP)

# Funkcja odpowiadająca za krok wroga w trakcie walki

def enemy_turn(target, target_AR, HP, DF, CT_enemy):
        # Battle variables
        Hero_HP = int(class_HP[HP])
        Hero_DF = int(class_DF[DF])
        # Battle equations
        Targ_AR = int(enemy_AR[target_AR])
        Enemy_attack = Hero_DF - Targ_AR * CT_enemy
        Hero_HP_after_Enemy_attack = Hero_HP + Enemy_attack

        if Enemy_attack < 0:
            print(enemies_upper[target] + " atakuje. "
            "Dostałeś/aś " + str(abs(Enemy_attack)) + " punktów obrażeń. "
            "Twoje zdrowie jest: " + str(Hero_HP_after_Enemy_attack) + " HP.\n")

            with open("../RPG game/txt_files/Hero_HP.txt", 'w', encoding="UTF-8") as BL:
                BL.write(str(Hero_HP_after_Enemy_attack))

        if Hero_HP_after_Enemy_attack > Hero_HP:
            print("\nUniknąłeś/ęłaś ataku.\n")

            return Hero_HP_after_Enemy_attack