from random import randint, choice
from brain_games.games.constants import CALC_TASK, MATH_OPERATORS
from brain_games.games.all_games import start_game


def get_math_expression():
    return f'{randint(1, 35)} {choice(MATH_OPERATORS)} {randint(1, 35)}'


def check_expression_result(expression):
    return str(eval(expression))


def new_game():
    start_game(CALC_TASK, get_math_expression, check_expression_result)
