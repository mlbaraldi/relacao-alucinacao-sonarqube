
def pluck(arr):
    smallest_even = float('inf')
    smallest_index = -1
    for i, node in enumerate(arr):
        if node % 2 == 0 and node < smallest_even:
            smallest_even = node
            smallest_index = i
    if smallest_index == -1:
        return []
    else:
        return [smallest_even, smallest_index]
