import random
import brain_games.cli as cli


def is_even():
    number = random.randint(1, 100)
    print(f'Question: {number}')

    user_answer = input('Your answer: ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    is_correct = user_answer == correct_answer

    return is_correct, user_answer, correct_answer

def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        is_correct, user_answer, right_answer = is_even()

        if is_correct:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    
    if count == 3:
        print(f'Congratulations, {name}!')



