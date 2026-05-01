from brain_games.cli import welcome_user
import brain_games.games.is_even as game
import brain_games.engine as engine


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    engine.play(game.is_even, user_name)



