
# Funkcja przekazująca pełnę nazwę potwora
def enemy_encountered_list_name(move):
    if move == "O":
        name = "Ogre"
    if move == "T":
        name = "Trol"
    if move == "W":
        name = "Wolf"
    if move == "R":
        name = "Rat"
    if move == "G":
        name = "Goblin"
    return name

# Funkcja przekazująca symbol dla każdego potwora
def enemy_encountered_list_letter(move):
    if move == "O":
        letter = "O"
    if move == "T":
        letter = "T"
    if move == "W":
        letter = "W"
    if move == "R":
        letter = "R"
    if move == "G":
        letter = "G"
    return letter