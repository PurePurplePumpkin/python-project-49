import prompt
from brain_games.constants import NUM_ROUNDS


def start_game(game_task, create_question_and_get_answer):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')

    print(f'Hello, {name}!\n'
          f'{game_task}')

    for _ in range(NUM_ROUNDS):
        question, right_ans = create_question_and_get_answer()
        ans = prompt.string(f'Question: {question}\n'
                            'Your answer: ')
        if ans == right_ans:
            print('Correct!')
        else:
            print(f'"{ans}" is wrong answer ;(. '
                  f'Correct answer was "{right_ans}".\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
