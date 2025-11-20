import random

def generate_question():
    n = random.randint(1, 100)
    return str(n), "yes" if n % 2 == 0 else "no"

def run():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    from VD_games.engine import play_game
    play_game(description, generate_question)
