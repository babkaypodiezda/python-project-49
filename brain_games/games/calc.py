import random


def calculate():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    question = f'{number1} {operator} {number2}'
    print(f'Question: {question}')

    user_answer = input('Your answer: ')
    correct_answer = str(eval(question))
    is_correct = user_answer == correct_answer

    return is_correct, user_answer, correct_answer