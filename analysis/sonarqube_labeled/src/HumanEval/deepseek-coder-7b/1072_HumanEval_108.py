
def count_nums(arr):
    def sum_of_digits(n):
        if n < 0:
            n = -n
        return sum(int(digit) for digit in str(n))

    return sum(1 for num in arr if sum_of_digits(num) > 0)

# Test cases
