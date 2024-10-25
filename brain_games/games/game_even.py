from random import randint
from brain_games.constants import EVEN_TASK
from brain_games.general_logic import start_game


def get_random_num_and_check_even():
    num = randint(1, 100)
    even = 'yes' if num % 2 == 0 else 'no'
    return (num, even)


def new_game():
    start_game(EVEN_TASK, get_random_num_and_check_even)
