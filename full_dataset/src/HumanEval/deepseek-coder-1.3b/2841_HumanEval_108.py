
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = -1 * num
        num_str = str(num)
        sum_digits = sum(int(digit) for digit in num_str)
        if sum_digits > 0:
            count += 1
    return count
