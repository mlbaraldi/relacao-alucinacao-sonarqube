
def pluck(arr):
    smallest_even_value = None
    smallest_index = None
    for i, node in enumerate(arr):
        if node % 2 == 0 and (smallest_even_value is None or node < smallest_even_value):
            smallest_even_value = node
            smallest_index = i
    if smallest_even_value is not None:
        return [smallest_even_value, smallest_index]
    else:
        return []
