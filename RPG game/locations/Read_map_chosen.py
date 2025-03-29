
# Funkcja otwierająca informację o zapisanej mapie w pliku Map_chosen.txt i oddaje literę, np. C
def RM():
    with open("../RPG game/txt_files/Map_chosen.txt", "r", encoding="UTF-8") as Map:
        for map_chosen in Map:
            Map.read()
    return str(map_chosen)