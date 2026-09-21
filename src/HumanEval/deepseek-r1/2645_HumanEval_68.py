
def pluck(arr):
    min_val = None
    min_index = -1
    for index, value in enumerate(arr):
        if value % 2 == 0:
            if min_val is None:
                min_val = value
                min_index = index
            elif value < min_val:
                min_val = value
                min_index = index
    return [min_val, min_index] if min_val is not None else []
