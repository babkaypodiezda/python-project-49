import random
import math

 
def is_prime(num):
    if num < 2: 
        return 'no'
    prime_number = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))

    return 'yes' if prime_number else 'no'


def prime():
    number = random.randint(1, 100)
    correct_answer = is_prime(number)
    question = str(number)
    
    return question, correct_answer
