
def digits(n):
    product = 1
    all_even = True
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            all_even = False
    return product if not all_even else 0
