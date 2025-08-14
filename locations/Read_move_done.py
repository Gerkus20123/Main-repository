
# Funkcja odczytuje zrobiony krok wykonany postacią w trakcie poruszania się po mapie z pliku Made Move.txt
# i oddaje tę liczbę w postaci string

def RMD():
    with open("../RPG game/txt_files/Made Move.txt", "r", encoding="utf-8") as f:
        for move in f:
            f.read()
    return move