
from characters.warrior import Warrior_status
from characters.mage import Mage_status
from characters.archer import Archer_status

# Funkcja wybierająca klasę postaci i zapisująca ten wybór w pliku Chosen_class.txt w postaci litery, np. W
def write_class(question_hero_class_choice):

    if question_hero_class_choice == "1":
        print("Wybrałeś/aś klasę: " + Warrior_status["Class"] + "\n")
        with open("../RPG game/txt_files/Chosen_class.txt", 'w', encoding="utf-8") as GFL:
            GFL.write("W")
            GFL.close()

    if question_hero_class_choice == "2":
        print("Wybrałeś/aś klasę: " + Mage_status["Class"] + "\n")
        with open("../RPG game/txt_files/Chosen_class.txt", 'w', encoding="utf-8") as GFL:
            GFL.write("M")
            GFL.close()

    if question_hero_class_choice == "3":
        print("Wybrałeś/aś klasę: " + Archer_status["Class"] + "\n")
        with open("../RPG game/txt_files/Chosen_class.txt", 'w', encoding="utf-8") as GFL:
            GFL.write("A")
            GFL.close()
    return

