class Troll:
    def __init__(self, HF, AR, DF):
        self.HF = HF
        self.AR = AR
        self.DF = DF

    def __str__(self):
        return f"Troll, zdrowie: {self.HF}, liczba obrarzeń: {self.AR}, obrona: {self.DF}"
# Troll, zdrowie: 15, liczba obrarzeń: 8, obrona: 12

if __name__ == "__main__":
    troll = Troll(10, 5, 12)
    print(troll)