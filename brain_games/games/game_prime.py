from random import randint
from brain_games.constants import PRIME_TASK
from brain_games.general_logic import start_game


def check_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_random_num_and_its_prime():
    num = randint(1, 101)
    prime = 'yes' if check_prime(num) else 'no'
    return (num, prime)


def new_game():
    start_game(PRIME_TASK, get_random_num_and_its_prime)
