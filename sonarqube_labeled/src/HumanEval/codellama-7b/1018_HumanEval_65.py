
def circular_shift(x, shift):
    # Get the number of digits in x
    num_digits = len(str(x))

    # If shift is greater than the number of digits, return the digits reversed
    if shift > num_digits:
        return str(x)[::-1]

    # Get the digits of x as a list
    digits = list(str(x))

    # Shift the digits right by shift
    for i in range(shift):
        digits.append(digits.pop(0))

    # Join the shifted digits back into a string
    return "".join(digits)
