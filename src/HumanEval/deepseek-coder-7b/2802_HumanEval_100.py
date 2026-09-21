
def make_a_pile(n):
    pile = []
    for i in range(n):
        if n % 2 == 0:
            n += 1
        pile.append(n)
        if n % 2 == 0:
            n += 1
    return pile
