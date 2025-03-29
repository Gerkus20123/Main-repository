from locations.Read_map_chosen import RM
from locations.Create_random_map_function import max_size_of_map_chosen
from Cube_Throw.Cube_throw_for_movement import CT
from locations.Read_move_done import RMD
from Consequence import consequence

# Funkcja wykonująca krok po mapie
def movement_1(move_done):
    question_hero_move = input(
        "Twoja pozycja na mapie jest: " + str(move_done) + " z " + max_size_of_map_chosen(
            RM()) + ". Gdzie chcesz iść? (1 - dalej czy 2 - wstecz):\n")

    if question_hero_move == "1":
        hero_move_forward = CT() + int(move_done)
        with open("../RPG game/txt_files/Made Move.txt", "w", encoding="UTF-8") as f:
            f.write(str(hero_move_forward))
            f.close()

        print("Ruszasz się na klatkę " + str(hero_move_forward) + " z " + max_size_of_map_chosen(RM()) + ".\n")

    if question_hero_move == "2":
        hero_move_backward = int(move_done) - CT()
        with open("../RPG game/txt_files/Made Move.txt", "w", encoding="UTF-8") as f:
            f.write(str(hero_move_backward))
            f.close()
        print("Ruszasz się na klatkę " + str(hero_move_backward) + " z " + max_size_of_map_chosen(RM()) + ".\n")
    return move_done

# Funkcja wykonująca współpracująca z funkcją movement_1() oraz consequence()
def movement_2(map_size, map):
    while True:
        print("Mapa: ", map)
        consequence(int(RMD()), map)
        movement_1(int(RMD()))
        if int(RMD()) >= int(max_size_of_map_chosen(map_size)):
            break
    with open("../RPG game/txt_files/Made Move.txt", 'w', encoding="utf-8") as f:
        f.write("1")
        f.close()
    with open("../RPG game/txt_files/Created_map.txt", 'w', encoding="utf-8") as MC:
        MC.write("")
        MC.close()