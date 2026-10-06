
def eat(number, need, remaining):
    eaten = number + need
    left = remaining - need
    if left < 0:
        left = 0
    return [eaten, left]
