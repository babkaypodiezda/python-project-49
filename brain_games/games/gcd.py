import random


def nod():
  number1 = random.randint(1, 100)
  number2 = random.randint(1, 100)
  print(f'Question: {number1} {number2}')
  user_answer = input('Your answer: ')

  a, b = max(number1, number2), min(number1, number2)
  while b:
      a, b = b, a % b
  
  correct_answer = str(a)
  is_correct = user_answer == correct_answer
  return is_correct, user_answer, correct_answer
