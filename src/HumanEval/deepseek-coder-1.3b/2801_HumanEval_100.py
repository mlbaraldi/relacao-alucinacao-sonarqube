
def make_a_pile(n):
    pile = [n]
    while True:
        n = n + 2 if n % 2 == 0 else n + 1
        pile.append(n)
        if n > pile[-1]:
            break
    return pile
