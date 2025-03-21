class Mage:
    def __init__(self, HF, AR, DF, MN):
        self.HF = HF
        self.AR = AR
        self.DF = DF
        self.MN = MN

    def attack(self, target, target_HF, HF):
        print(f"Mag atakuje {target}a mieczem. Zdrowie Maga jest {HF}, zdrowie {target} jest {target_HF}.")

    def block(self, target, target_HF, HF, DF):
        print(f"Mag blokuje {target}a. Zdrowie i obrona Maga są {HF}, {DF + 2}, zdrowie {target}a jest {target_HF}.")

    def prepare(self, HF, AR):
        print(f"Mag przygotowuje się do ataku w następnej turze. Zdrowie Mag jest {HF}, punkty obrarzeń są {AR + 3}.")

    def escape(self):
        print(f"Ucieczka.")

    def battle_won(self, target):
        print(f"Mag pokonał {target}")

    def item_recieved(self, item, gold):
        print(f"Mag otrzymuje /{item}/ oraz {gold} Gold")

    def use_spell(self, spell, target):
        print(f"Mag rzuca zaklęcie {spell} na {target}")

    def __str__(self):
        return f"Wojownik ma {self.HF} zdrowia, {self.AR} wielkości obrarzeń oraz {self.DF} punktów obrony."