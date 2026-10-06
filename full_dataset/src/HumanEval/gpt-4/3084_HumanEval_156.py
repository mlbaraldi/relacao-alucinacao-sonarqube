
def int_to_mini_roman(number):
    if not 1 <= num <= 1000:
        return "Number out of range. Please enter a number between 1 and 1000."

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]

    res = ""
    for i in range(len(values)):
        count = num // values[i]
        res += numerals[i] * count
        num %= values[i]

    return res
