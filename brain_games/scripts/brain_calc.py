import brain_games.cli as cli
import brain_games.games.calc as game
import brain_games.engine as play


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    print('What is the result of the expression?')

    play.play(game.calculate, user_name)