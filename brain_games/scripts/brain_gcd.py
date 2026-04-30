import brain_games.cli as cli
import brain_games.games.gcd as game
import brain_games.engine as play


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')

    play.play(game.nod, user_name)