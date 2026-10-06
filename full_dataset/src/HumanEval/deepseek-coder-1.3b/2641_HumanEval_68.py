
def pluck(arr):
    smallest_even = None
    smallest_index = None
    for i, num in enumerate(arr):
        if num % 2 == 0 and (smallest_even is None or num < smallest_even):
            smallest_even = num
            smallest_index = i
    return [smallest_even, smallest_index] if smallest_even is not None else []
