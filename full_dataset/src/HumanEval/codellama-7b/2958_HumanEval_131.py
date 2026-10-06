
def digits(n):
    if n < 0:
        raise ValueError("n must be a positive integer")
    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        n //= 10
    return product
