import random
import math

 
def is_prime(num):
    if num < 2: return 'no'
    return 'yes' if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)) else 'no'
  
def prime():
    number = random.randint(1, 100)
    correct_answer = is_prime(number)
    question = str(number)
    
    return question, correct_answer
