
# Funkcja odczytująca klasę postaci z pliku Chosen_class.txt i przekazująca zapisaną tam literę na zewnątrz
def read_class():
    with open("../RPG game/txt_files/Chosen_class.txt", 'r', encoding="utf-8") as GFL:
        for word in GFL:
            GFL.read()
    return word