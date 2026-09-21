
def count_nums(arr):
    def sum_digits(n):
        if n == 0:
            return 0
        is_negative = n < 0
        abs_n = abs(n)
        digits = []
        while abs_n > 0:
            digits.append(abs_n % 10)
            abs_n = abs_n // 10
        digits = digits[::-1]
        if is_negative and digits:
            digits[0] *= -1
        return sum(digits)
    
    count = 0
    for num in arr:
        if num == 0:
            continue
        s = sum_digits(num)
        if s > 0:
            count += 1
    return count
