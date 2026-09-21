
def is_equal_to_sum_even(n):
    if n % 2 != 0:
        return False
    count = 0
    for i in range(2, n + 1, 2):
        if n - i == 0:
            count += 1
        elif n - i < 0:
            break
        else:
            continue
    return count == 4
