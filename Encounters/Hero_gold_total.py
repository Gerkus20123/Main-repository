
def hero_GL_T():
    with open("../RPG game/txt_files/Hero_gold_obtained.txt", 'r', encoding="UTF-8") as f:
        for gold in f:
            f.read()
    return gold


def Hero_GL_T_calc(gold_previous_move, gold_obtained):
    gold_next_move = gold_previous_move + gold_obtained
    return gold_next_move