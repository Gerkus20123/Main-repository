class Warrior:
    def __init__(self, HF, AR, DF):
        self.HF = HF
        self.AR = AR
        self.DF = DF

    def attack(self, target, target_HF, HF):
        print(f"Wojownik atakuje {target}a mieczem. Zdrowie Wojownika jest {HF}, zdrowie {target} jest {target_HF}.")

    def block(self, target, target_HF, HF, DF):
        print(f"Wojownik blokuje {target}a. Zdrowie i obrona Wojownika są {HF}, {DF + 2}, zdrowie {target}a jest {target_HF}.")

    def prepare(self, HF, AR):
        print(f"Wojownik przygotowuje się do ataku w następnej turze. Zdrowie Wojownika jest {HF}, punkty obrarzeń są {AR + 3}.")

    def escape(self):
        print(f"Ucieczka.")

    def battle_won(self, target):
        print(f"Wojownik pokonał {target}")

    def item_recieved(self, item, gold):
        print(f"Wojownik otrzymuje /{item}/ oraz {gold} Gold")

    def __str__(self):
        return f"Wojownik ma {self.HF} zdrowia, {self.AR} wielkości obrarzeń oraz {self.DF} punktów obrony."

if __name__ == "__main__":
    Health = Warrior(25, 5, 10)
    print(Health)

    enemy_attack = Health.attack("szczur", 3, 25)
    enemy_block = Health.block("szczur", 3, 25, 10)
    enemy_prepare = Health.prepare(25, 5)
    warrior_escape = Health.escape()
    enemy_defeated = Health.battle_won("szczur")
    item = Health.item_recieved("Health Elexir", 5)

    # player = Warrior(2, 2, 2)
    # player.atack("szczur", wartoszc
    # 'wartosc)