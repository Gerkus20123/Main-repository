# Class Mage has 15 HP, 3 AR, 4 DF, 15 MN
# Can use two spells:
# - Fireball = 8 AR, MNC 4
# - Blessing = 5 HP up, MNC 5

Mage_status = {"Class": "Mag",
               "HP": "15",
               "AR": "3",
               "DF": "4",
               "MN": "15"}

Spell_Fireball = {"Spell": "Fireball",
                  "AR": "8",
                  "MNC": "4"}

Spell_Blessing = {"Spell": "Blessing",
                  "HPup": "5",
                  "MNC": "5"}

class Mage:

    def hero_status(self, HP, AR, DF, MN):
        return f"Masz {HP} HP, {AR} AR, {DF} DF oraz {MN} MN."

    def attack(self, target, target_HP):
        return f"Atakujesz {target}a mieczem. Zdrowie {target}a jest {target_HP} HP."

    def block(self, target, DF):
        return f"Blokujesz {target}a. Twoje punkty obrony wyrosły do {DF} DF."

    def prepare(self, AR):
        return f"Jesteś przygotowany do ataku w następnej turze. Punkty obrażeń wyrosły do {AR} AR."

    def escape(self):
        return f"Ucieczka."

    def battle_won(self, target):
        return f"Pokonałeś/aś {target}a."

    def item_recieved(self, item):
        return f"Otrzymujesz {item}."

    def gold_recieved(self, gold):
        return f"Otrzymujesz {gold} Gold."

    def use_spell_fireball(self, target, target_HP, MN):
        return f"Rzucasz zaklęcie Fireball na {target}a, {target} ma {target_HP} HP. Masz {MN - 4} MN."

    def use_spell_blessing(self, HP, MN):
        return f"Wywołujesz zaklęcie Blessing. Masz {HP + 5} HP oraz {MN - 5} MN."

# Sprawdzenie klasy
# if __name__ == "__main__":
#     Status = Mage().hero_status(15, 3, 4, 15)
#     Hero_attacks = Mage().attack("szczur", 10)
#     Hero_blocks = Mage().block("szczur", 4)
#     Hero_prepares = Mage().prepare(3)
#     Hero_escapes = Mage().escape()
#     Hero_defeats_enemy = Mage().battle_won("szczur")
#     Hero_recieves_item = Mage().item_recieved("Health Elexir", 5)
#     Hero_recieves_gold = Mage().gold_recieved(5)
#     Hero_uses_spell_fireball = Mage().use_spell_fireball("szczur", 10, 15)
#     Hero_uses_spell_blessing = Mage().use_spell_blessing(15, 15)