import prompt
from random import randint


NUM_ROUNDS = 3


def check_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def new_game():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')

    print(f'Hello, {name}!\n'
          'Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(NUM_ROUNDS):
        num = randint(1, 100)
        ans = prompt.string(f'Question: {num}\n'
                            'Your answer: ')
        right_ans = check_even(num)
        if ans == right_ans:
            print('Correct!')
        else:
            print(f'"{ans}" is wrong answer ;(. '
                  f'Correct answer was "{right_ans}".\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
