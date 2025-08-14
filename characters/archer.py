# Class Archer has 20 HP, 4 AR, 6 DF

Archer_status = {"Class": "Łucznik",
                 "HP": "20",
                 "AR": "4",
                 "DF": "6"}

class Archer:

    def hero_status(self, HP, AR, DF):
        return f"Masz {HP} HP, {AR} AR oraz {DF} DF."

    def attack(self, target, target_HP):
        return f"Strzelasz do {target}a z łuku. Zdrowie {target}a jest {target_HP} HP."

    def block(self, target, DF):
        return f"Blokujesz {target}a. Twoje punkty obrony wyrosły do {DF} DF."

    def prepare(self, AR):
        return f"Jesteś przygotowany do ataku w następnej turze. Punkty obrażeń wyrosły do {AR} DF."

    def escape(self):
        return f"Ucieczka."

    def battle_won(self, target):
        return f"Pokonałeś/aś {target}a."

    def item_recieved(self, item):
        return f"Otrzymujesz {item}."

    def gold_recieved(self, gold):
        return f"Otrzymujesz {gold} Gold."

# Sprawdzenie klasy
# if __name__ == "__main__":
#
#     Status = Archer().hero_status(20, 4, 6)
#     Hero_attacks = Archer().attack("szczur", 10)
#     Hero_blocks = Archer().block("szczur", 10)
#     Hero_prepares = Archer().prepare(5)
#     Hero_escapes = Archer().escape()
#     Hero_defeats_enemy = Archer().battle_won("szczur")
#     Hero_recieves_item = Archer().item_recieved("Health Elexir")
#     Hero_recieves_gold = Archer().gold_recieved(5)