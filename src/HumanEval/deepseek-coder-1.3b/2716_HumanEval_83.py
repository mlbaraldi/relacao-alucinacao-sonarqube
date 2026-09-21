
def starts_one_ends(n):
    count = 0
    lower_bound = 10 ** (n - 1)
    upper_bound = 10 ** n
    for num in range(lower_bound, upper_bound):
        str_num = str(num)
        if str_num[0] == '1' or str_num[-1] == '1':
            count += 1
    return count
