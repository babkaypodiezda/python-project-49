import random


def row_numbers():
   length = random.randint(5, 10)
   start, step = random.randint(1, 30), random.randint(1, 30)
   row = [start + step * index for index in range(length)]

   random_index = random.randint(0, length - 1)
   answer, row[random_index] = row[random_index], "..."
   row = ' '.join(str(x) for x in row)
   return answer, row

 
def progression():
  answer, row = row_numbers()
  question = row
  correct_answer = str(answer)

  return question, correct_answer