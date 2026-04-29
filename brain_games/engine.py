def play(game, user_name):
    count = 0
    while count < 3:
        is_correct, user_answer, right_answer = game()

        if is_correct:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    
    if count == 3:
        print(f'Congratulations, {user_name}!')