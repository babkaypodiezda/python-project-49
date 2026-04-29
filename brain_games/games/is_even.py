import random


def is_even():
    number = random.randint(1, 100)
    print(f'Question: {number}')

    user_answer = input('Your answer: ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    is_correct = user_answer == correct_answer

    return is_correct, user_answer, correct_answer