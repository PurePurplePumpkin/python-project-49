from random import randint
from brain_games.games.constants import PROGRESSION_TASK
from brain_games.games.constants import MAX_LEN_PROGRESSION, MIN_LEN_PROGRESSION
from brain_games.games.all_games import start_game


def get_progression_and_skip_num():
    len_progression = randint(MIN_LEN_PROGRESSION, MAX_LEN_PROGRESSION)
    step = randint(2, 9)
    start = randint(2, 15)
    skip_i = randint(0, len_progression - 1)
    skip_num = str(start + skip_i * step)
    progression_lists = []

    for i in range(len_progression):
        if i == skip_i:
            progression_lists.append('..')
        else:
            progression_lists.append(str(start + i * step))

    return (' '.join(progression_lists), skip_num)


def new_game():
    start_game(PROGRESSION_TASK, get_progression_and_skip_num)
