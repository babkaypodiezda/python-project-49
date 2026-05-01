import random


def nod():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    a, b = max(number1, number2), min(number1, number2)
    while b:
        a, b = b, a % b
  
    question = f'{str(number1)} {str(number2)}'
    correct_answer = str(a)

    return question, correct_answer
