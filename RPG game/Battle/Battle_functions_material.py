from characters.warrior import Warrior, Warrior_status
from characters.mage import Mage, Mage_status, Spell_Fireball, Spell_Blessing
from characters.archer import Archer, Archer_status

from Encounters.monsters.goblin import Goblin_status, Goblin_enemy_name, Goblin_enemy_name_upper
from Encounters.monsters.ogre import Ogre_status, Ogre_enemy_name, Ogre_enemy_name_upper
from Encounters.monsters.rat import Rat_status, Rat_enemy_name, Rat_enemy_name_upper
from Encounters.monsters.troll import Troll_status, Troll_enemy_name, Troll_enemy_name_upper
from Encounters.monsters.wolf import Wolf_status, Wolf_enemy_name, Wolf_enemy_name_upper

# Zmienne do funkcji walki (Battle functions) - Przeciwniki (Enemies)

enemies = {"G": Goblin_enemy_name,
           "O": Ogre_enemy_name,
           "R": Rat_enemy_name,
           "T": Troll_enemy_name,
           "W": Wolf_enemy_name}

enemies_upper = {"G": Goblin_enemy_name_upper,
                 "O": Ogre_enemy_name_upper,
                 "R": Rat_enemy_name_upper,
                 "T": Troll_enemy_name_upper,
                 "W": Wolf_enemy_name_upper}

enemy_HP = {"G": Goblin_status["HP"],
            "O": Ogre_status["HP"],
            "R": Rat_status["HP"],
            "T": Troll_status["HP"],
            "W": Wolf_status["HP"]}

enemy_DF = {"G": Goblin_status["DF"],
            "O": Ogre_status["DF"],
            "R": Rat_status["DF"],
            "T": Troll_status["DF"],
            "W": Wolf_status["DF"]}

enemy_AR = {"G": Goblin_status["AR"],
            "O": Ogre_status["AR"],
            "R": Rat_status["AR"],
            "T": Troll_status["AR"],
            "W": Wolf_status["AR"]}

# Zmienne do funkcji walki (Battle functions) - Postaci (Heroes)
classes = {"W": Warrior(),
           "M": Mage(),
           "A": Archer()}

class_HP = {"W": Warrior_status["HP"],
            "M": Mage_status["HP"],
            "A": Archer_status["HP"]}

class_DF = {"W": Warrior_status["DF"],
            "M": Mage_status["DF"],
            "A": Archer_status["DF"]}

class_AR = {"W": Warrior_status["AR"],
            "M": Mage_status["AR"],
            "A": Archer_status["AR"]}

