from random import randint, choice
from brain_games.constants import CALC_TASK, MATH_OPERATORS
from brain_games.general_logic import start_game


def get_math_expression_and_chek_result():
    expression = f'{randint(1, 35)} {choice(MATH_OPERATORS)} {randint(1, 35)}'
    result = str(eval(expression))
    return (expression, result)


def new_game():
    start_game(CALC_TASK, get_math_expression_and_chek_result)
