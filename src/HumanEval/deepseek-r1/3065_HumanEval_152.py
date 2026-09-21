
def compare(game,guess):
    return [abs(g - u) for g, u in zip(game, guess)]
