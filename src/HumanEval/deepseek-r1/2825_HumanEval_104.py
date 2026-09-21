
def unique_digits(x):
    def has_all_odd_digits(n):
        s = str(n)
        for ch in s:
            if int(ch) % 2 == 0:
                return False
        return True

    result = []
    for num in x:
        if has_all_odd_digits(num):
            result.append(num)
    result.sort()
    return result
