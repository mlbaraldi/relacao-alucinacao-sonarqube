
def max_fill(grid, capacity):
    import math
    import math
    count = 0
    for row in grid:
        if sum(row) > 0:
            count += math.ceil(sum(row) / capacity)
    return count
