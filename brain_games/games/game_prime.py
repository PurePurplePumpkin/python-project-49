from random import randint
from brain_games.constants import PRIME_TASK
from brain_games.general_logic import start_game


def get_random_num_and_check_prime():
    num = randint(1, 101)
    prime = 'yes'

    if num < 2:
        prime = 'no'
        return (num, prime)

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = 'no'
            return (num, prime)

    return (num, prime)


def new_game():
    start_game(PRIME_TASK, get_random_num_and_check_prime)
