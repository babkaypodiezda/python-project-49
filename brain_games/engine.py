def play(game, user_name):
    count = 0
    while count < 3:
         question, correct_answer = game()
         print(f'Question: {question}')
         user_answer = input('Your answer: ')

         if user_answer == correct_answer:
             print('Correct!')
             count += 1
         else:
             print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
             print(f"Let's try again, {user_name}!")
             break
    
    if count == 3:
        print(f'Congratulations, {user_name}!')