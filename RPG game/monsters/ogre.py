class Ogre:
    def __init__(self, HF, AR, DF):
        self.HF = HF
        self.AR = AR
        self.DF = DF

    def __str__(self):
        return f"Ogr, zdrowie: {self.HF}, liczba obrarzeń: {self.AR}, obrona: {self.DF}"
# Ogr, zdrowie: 15, liczba obrarzeń: 8, obrona: 12

if __name__ == "__main__":
    ogre = Ogre(15, 8, 12)
    print(ogre)