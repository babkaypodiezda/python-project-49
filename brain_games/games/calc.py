import random


def calculate():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    question = f'{number1} {operator} {number2}'
    correct_answer = str(eval(question))

    return question, correct_answer