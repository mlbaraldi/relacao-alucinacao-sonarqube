
def specialFilter(nums):
    count = 0
    for num in nums:
        if num <= 10:
            continue
        abs_num = abs(num)
        last_digit = abs_num % 10
        str_num = str(abs_num)
        first_digit = int(str_num[0])
        if first_digit % 2 == 1 and last_digit % 2 == 1:
            count += 1
    return count
