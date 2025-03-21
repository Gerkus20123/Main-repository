class Rat:
    def __init__(self, HF, AR, DF):
        self.HF = HF
        self.AR = AR
        self.DF = DF

    def __str__(self):
        return f"Rat, zdrowie: {self.HF}, liczba obrarzeń: {self.AR}, obrona: {self.DF}"
# Rat, zdrowie: 7, liczba obrarzeń: 2, obrona: 3

if __name__ == "__main__":
    rat = Rat(3, 1, 1)
    print(rat)