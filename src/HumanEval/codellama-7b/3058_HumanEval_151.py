
def double_the_difference(lst):
    if not lst:
        return 0
    odd_numbers = [x for x in lst if x % 2 != 0 and x > 0]
    return sum([x**2 for x in odd_numbers]) * 2
