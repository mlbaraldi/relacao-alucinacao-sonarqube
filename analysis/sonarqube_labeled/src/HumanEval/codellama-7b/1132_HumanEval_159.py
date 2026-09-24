
def eat(number, need, remaining):
    if number > remaining:
        return [remaining, 0]
    else:
        return [number + need, remaining - number]
