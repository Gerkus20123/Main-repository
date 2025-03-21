class Goblin:
    def __init__(self, HF, AR, DF):
        self.HF = HF
        self.AR = AR
        self.DF = DF

    def __str__(self):
        return f"Goblin, zdrowie: {self.HF}, liczba obrarzeń: {self.AR}, obrona: {self.DF}"
# Goblin, zdrowie: 7, liczba obrarzeń: 2, obrona: 3

if __name__ == "__main__":
    goblin = Goblin(7, 2, 3)
    print(goblin)