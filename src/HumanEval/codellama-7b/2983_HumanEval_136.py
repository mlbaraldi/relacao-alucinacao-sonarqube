
def largest_smallest_integers(lst):
    largest_negative = None
    smallest_positive = None

    for i in lst:
        if i < 0 and (largest_negative is None or i > largest_negative):
            largest_negative = i
        elif i > 0 and (smallest_positive is None or i < smallest_positive):
            smallest_positive = i

    return (largest_negative, smallest_positive)
