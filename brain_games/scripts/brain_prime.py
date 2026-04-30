import brain_games.cli as cli
import brain_games.games.prime as game
import brain_games.engine as engine


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    engine.play(game.prime, user_name)