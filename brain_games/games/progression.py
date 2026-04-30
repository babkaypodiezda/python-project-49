import random


def row_numbers():
   length = random.randint(5, 10)
   start, step = random.randint(0, 30), random.randint(0, 30)
   row = [start + step * index for index in range(length)]

   random_index = random.randint(0, length - 1)
   answer, row[random_index] = row[random_index], "..."
   row = ' '.join(str(x) for x in row)
   return answer, row

 
def progression():
  answer, row = row_numbers()
  print(f'Question: {row}')
  user_answer = input('Your answer: ')
  correct_answer = str(answer)
  is_correct = user_answer == correct_answer
  return is_correct, user_answer, correct_answer