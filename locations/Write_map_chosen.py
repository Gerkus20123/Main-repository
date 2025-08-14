
# Funkcja zapisująca symbol wybranej mapy w zależności od zapytania, które idzie zewnątrz funkcji
def write_chosen_map(question_map_choice):
    if question_map_choice == "1":
        print("Wybrałeś/aś mapę: Loch\n")
        with open("../RPG game/txt_files/Map_chosen.txt", 'w', encoding="utf-8") as MC:
            MC.write("C")
            MC.close()
    if question_map_choice == "2":
        print("Wybrałeś/aś mapę: Las \n")
        with open("../RPG game/txt_files/Map_chosen.txt", 'w', encoding="utf-8") as MC:
            MC.write("F")
            MC.close()
    if question_map_choice == "3":
        print("Wybrałeś/aś mapę: Miasto \n")
        with open("../RPG game/txt_files/Map_chosen.txt", 'w', encoding="utf-8") as MC:
            MC.write("M")
            MC.close()
