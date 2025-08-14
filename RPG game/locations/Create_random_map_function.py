import random

# Funkcja stwarza mapę i zapisuje ją w pliku zewnętrznym Created_map.txt
def create_map(question_map_choice):

    encounter_list = ["G", "W", "R", "T", "O", "GL", "GL", "GL", "GL", "Merchant", "Item", "Empty", "Empty", "Empty"]

    if question_map_choice == "1":

        lista_values = []
        lista_keys = []
        map_size = [i for i in range(1, 16)]

        for value in map_size:
            lista_values.insert(1, random.choice(encounter_list))

        for key in map_size:
            lista_keys.append(key)

        map = dict(zip(lista_keys, lista_values))
        # print(map)

    if question_map_choice == "2":

        lista_values = []
        lista_keys = []
        map_size = [i for i in range(1, 51)]

        for value in map_size:
            lista_values.insert(1, random.choice(encounter_list))

        for key in map_size:
            lista_keys.append(key)

        map = dict(zip(lista_keys, lista_values))
        # print(map)

    if question_map_choice == "3":

        lista_values = []
        lista_keys = []
        map_size = [i for i in range(1, 101)]

        for value in map_size:
            lista_values.insert(1, random.choice(encounter_list))

        for key in map_size:
            lista_keys.append(key)

        map = dict(zip(lista_keys, lista_values))
    return map

# Funkcja przyjmuje mapę w postaci słownika (z funkcji Create_map()) oraz liczbę reprezentującą krok, np. 4 z 15 itd.
def move(map, turn):
    return str(map[turn])

# Funkcja przyjmuje mapę z pliku i oddaje wielkość mapy w postaci string
def max_size_of_map_chosen(map_chosen):
    if map_chosen == "C":
        mapp = "15"
    if map_chosen == "F":
        mapp = "50"
    if map_chosen == "M":
        mapp = "100"
    return mapp