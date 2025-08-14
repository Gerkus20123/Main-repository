
from random import choice as RC

# Funkcja tworząca losową liczbę od 1 do 6 dla postaci

def CT_hero():
    cube = [1, 2, 3, 4, 5, 6]
    cube_throw_hero = RC(cube)
    print("Rzucasz kostkę: " + str(cube_throw_hero) + " CT")
    return cube_throw_hero