import brain_games.cli as cli
import brain_games.games.progression as game
import brain_games.engine as engine


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    print('What number is missing in the progression?')

    engine.play(game.progression, user_name)