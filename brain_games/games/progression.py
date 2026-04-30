import random

 
def progression():
    length = random.randint(5, 10)
    start, step = random.randint(1, 30), random.randint(1, 30)
    row = [start + step * index for index in range(length)]

    random_index = random.randint(0, length - 1)
    answer, row[random_index] = row[random_index], "..."

    question = ' '.join(str(x) for x in row)
    correct_answer = str(answer)

    return question, correct_answer