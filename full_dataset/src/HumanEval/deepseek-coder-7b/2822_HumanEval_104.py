
def unique_digits(x):
    def has_even_digit(n):
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                return True
            n = n // 10
        return False

    return sorted(n for n in x if not has_even_digit(n))

