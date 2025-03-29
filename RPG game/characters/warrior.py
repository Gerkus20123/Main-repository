# Class Warrior has 25 HP, 5 AR, 10 DF

Warrior_status = {"Class": "Wojownik",
                  "HP": "25",
                  "AR": "5",
                  "DF": "10"}

class Warrior:

    def hero_status(self, HP, AR, DF):
        print (f"Masz {HP} HP, {AR} AR oraz {DF} DF.")

    def attack(self, target, target_HP):
        print(f"Atakujesz {target}a mieczem. Zdrowie {target}a jest {target_HP} HP.")

    def missed(self):
        print(f"Cel uniknął ataku.")

    def block(self, target, DF):
        print(f"Blokujesz {target}a. Twoje punkty obrony wyrosły do {DF} DF.")

    def prepare(self, AR):
        print(f"Jesteś przygotowany do ataku w następnej turze. Punkty obrażeń wyrosły do {AR} DF.")

    def escape(self):
        print(f"Ucieczka.")

    def battle_won(self, target):
        print(f"Pokonałeś/aś {target}a.")

    def item_recieved(self, item):
        print(f"Otrzymujesz {item}.")

    def gold_recieved(self, gold):
        print(f"Otrzymujesz {gold} Gold.")

# Sprawdzenie klasy
# if __name__ == "__main__":
#     Status = Warrior().hero_status(25, 5, 10)
#     Hero_attacks = Warrior().attack("szczur", 10)
#     Hero_blocks = Warrior().block("szczur", 10)
#     Hero_prepares = Warrior().prepare(5)
#     Hero_escapes = Warrior().escape()
#     Hero_defeats_enemy = Warrior().battle_won("szczur")
#     Hero_recieves_item = Warrior().item_recieved("Health Elexir")
#     Hero_recieves_gold = Warrior().gold_recieved(5)