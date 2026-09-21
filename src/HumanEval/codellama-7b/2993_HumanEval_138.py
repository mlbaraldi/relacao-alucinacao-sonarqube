
def is_equal_to_sum_even(n):
    if n % 2 == 0:
        return False
    for i in range(1, n):
        if i % 2 == 0 and n - i == 2:
            return True
    return False
