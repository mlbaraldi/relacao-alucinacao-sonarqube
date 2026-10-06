
def sort_array(array):
    if not array:
        return []
    sum_first_last = sum(array[0], array[-1])
    if sum_first_last % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
