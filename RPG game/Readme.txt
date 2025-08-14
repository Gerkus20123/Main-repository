----------------------------------------------| RPG game (Nighty Nights) |----------------------------------------------

---------------------------------------------------------OPIS-GRY-------------------------------------------------------

Wybierasz klasę postaci: wojownik (warrior), mag (mage) albo łucznik (archer), którzy prze-
chodzą przez mapę. W grze mamy 3 lokacji: miasto (city), loch (dangeon) oraz las (forest). 
Na każdej mapie jest punkt A (start) i punkt B (end). W punkcie A postać się pojawia na mapie 
i zaczyna swoję drogę przez mapę.
   Na mapie się generuje wraz ze wszystkimi przeszkodami też sklep, w którym możesz coś kupić 
np. elixir życia (health potion) oraz many (mana potion). Waluta gry jest zloty monety (gold).
Na mapie postać napotyka na swojej drodze przypadkowo różnych potworów np. goblin, troll itd.
Mapa jest tworzona przypadkowo oraz także lokalizacja potworów.
Zloty monety można znaleźć na mapie leżącej na klatce albo dostać po pokonaniu potwora w zale-
żności od siły potwora. Za każdego potwora daje się różna ilość monet.
Cel gry to dojść do punktu B.

------------------------------------------------------------SKRÓTY----------------------------------------------------------

Health - HF
Attack rating - AR
Defence - DF
Mana - MN
Mana cost - MNC
Gold - GL

---------------------------------------------------------OPIS-POSTACI-------------------------------------------------------
Każda postać ma swoi charakterystyki:

// Warrior//
HF = 25
AR = 5
DF = 10

// Mage //
HF = 15
MN = 15
AR = 3
DF = 4
Spell:
- Fireball = 8 AR, MNC 4
- Blessing = 5 HF up, MNC 5

// Archer //
HF = 20
AR = 4
DF = 6

---------------------------------------------------------OPIS-POTWORÓW-------------------------------------------------------

Każda postać ma swoi charakterystyki:

// Goblin //
HF = 7
AR = 2
DF = 3

// Wolf //
HF = 5
AR = 3
DF = 4

// Rat //
HF = 3
AR = 1
DF = 1

// Troll //
HF = 10
AR = 5
DF = 6

// Ogre //
HF = 15
AR = 8
DF = 12

---------------------------------------------------------MAPA---------------------------------------------------------------

Mapa jest liniowa. Wielkość mapy oraz długość gry zależą od typu.
- Dungeon (Loch) ma 15 klatek.
- Forest (Las) ma 50 klatek.
- City (miasto) ma 100 klatek

---------------------------------------------------------WALKA--------------------------------------------------------------

Walka jest turowa:

Najpierw się losuje, kto idzie pierwszym:
Postac rzuca kostkę (zestaw z 6 liczb), potem rzuca kostkę komputer, jeśli liczba jest wieksza dla postaci użytkownika, 
to on/ona idzie pierwsza. 

Dalej użytkownik ma następne kroki (actions):
- Attack
- Block the next enemy attack (+2 DF)
- Prepare (+3 AR in the next turn)
- Escape (Lose 5 HF and 2 GL).")

hero_damage = monster_DF - Hero_AR * cube_throw

monster_damage = Hero_DF - monster_AR * cube_throw

Walka się toczy aż potwór zostanie pokonany.
Jeśli wartość zdrowia jest równe zero albo ujemna = Zwycieżtwo


cube_throw = rzucenie kostki

--------------------------------------------------STRUKTURA-FOLDERU-Z-GRĄ---------------------------------------------------
RPG game
├── main.py
├── Consequence.py
├── Movement.py
├── Readme.txt
├── Battle/
│   ├── battle.py
│   ├── Battle_functions_material.py
│   ├── Enemy_turn.py
│   └── Hero_turn.py
├── characters/
│   ├── warrior.py
│   ├── mage.py
│   └── archer.py
├── Class_files/
│   ├── Chosen_class_read.py
│   └── Chosen_class_write.py
├── Class_files/
│   ├── Cube_throw_for_battle_enemy.py
│   ├── Cube_throw_for_battle_hero.py
│   └── Cube_throw_for_movement.py
├── Encounters/
│   ├── Hero_gold_total.py
│   ├── Items.py
│   ├── Shop.py
│   └── monsters/
│   	├── rat.py
│   	├── goblin.py
│   	├── wolf.py
│   	├── troll.py
│   	├── troll.py
│   	└── Enemies.py
├── locations/
│   ├── cave.py
│   ├── city.py
│   ├── forest.py
│   ├── Create_random_map_function.py
│   ├── Write_map_chosen.py
│   ├── Read_move_done.py
│   └── Read_map_chosen.py
├── txt_files/
│   ├── Chosen_class.txt
│   ├── Created_map.txt
│   ├── Hero_AR.txt
│   ├── Hero_DF.txt
│   ├── Hero_gold_obtained.txt
│   ├── Hero_HP.txt
│   ├── Hero_items_obtained.txt
│   ├── Hero_MN.txt
│   ├── Made Move.txt
│   ├── Map_chosen.txt
│   └── Target_HP.txt

