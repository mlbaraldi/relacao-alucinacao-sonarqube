
def max_fill(grid, capacity):
    import math
    total = 0
    for row in grid:
        s = sum(row)
        if s == 0:
            continue
        total += (s + capacity - 1) // capacity
    return total
