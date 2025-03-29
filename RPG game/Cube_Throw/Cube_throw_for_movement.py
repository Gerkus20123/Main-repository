from random import choice as RC

def CT():
    cube = [1, 2, 3, 4, 5, 6]
    cube_throw = RC(cube)
    print("Rzucasz kostkę: " + str(cube_throw) + " CT")
    return cube_throw