class Wolf:
    def __init__(self, HF, AR, DF):
        self.HF = HF
        self.AR = AR
        self.DF = DF

    def __str__(self):
        return f"Wilk, zdrowie: {self.HF}, liczba obrarzeń: {self.AR}, obrona: {self.DF}"
# Wilk, zdrowie: 7, liczba obrarzeń: 2, obrona: 3

if __name__ == "__main__":
    wolf = Wolf(5, 3, 4)
    print(wolf)