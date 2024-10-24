from math import gcd
from random import randint
from brain_games.games.constants import GCD_TASK
from brain_games.games.all_games import start_game


def get_nums_for_gcd():
    num_one, num_two, factor = randint(1, 20), randint(1, 20), randint(2, 5)
    return f'{num_one * factor} {num_two * factor}'


def check_gcd(nums):
    num_one, num_two = nums.split()
    return str(gcd(int(num_one), int(num_two)))


def new_game():
    start_game(GCD_TASK, get_nums_for_gcd, check_gcd)
