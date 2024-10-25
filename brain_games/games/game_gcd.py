from math import gcd
from random import randint
from brain_games.constants import GCD_TASK
from brain_games.general_logic import start_game


def get_nums_for_gcd_and_check_result():
    factor = randint(2, 5)
    num_one = randint(1, 20) * factor
    num_two = randint(1, 20) * factor
    nums_for_gcd = f'{num_one} {num_two}'
    result_gcd = str(gcd(num_one, num_two))
    return (nums_for_gcd, result_gcd)


def new_game():
    start_game(GCD_TASK, get_nums_for_gcd_and_check_result)
