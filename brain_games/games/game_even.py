from random import randint
from brain_games.games.constants import EVEN_TASK
from brain_games.games.all_games import start_game


def get_random_num():
    return randint(1, 100)


def check_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def new_game():
    start_game(EVEN_TASK, get_random_num, check_even)
