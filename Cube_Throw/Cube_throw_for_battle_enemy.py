from random import choice as RC

# Funkcja tworząca losową liczbę od 1 do 6 dla wroga
def CT_enemy():
    cube = [1, 2, 3, 4, 5, 6]
    cube_throw_enemy = RC(cube)
    print("Przeciwnik rzuca kostkę: " + str(cube_throw_enemy) + " CT")
    return cube_throw_enemy