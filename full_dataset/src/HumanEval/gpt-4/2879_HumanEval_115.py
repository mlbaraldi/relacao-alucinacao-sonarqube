
def max_fill(grid, capacity):
    import math
    # Calculate the total amount of water in all wells
    total_water = sum(sum(row) for row in grid)
    
    # Calculate the number of times you need to lower the buckets
    # by dividing the total amount of water by the bucket capacity
    # and rounding up to the nearest integer
    return (total_water + capacity - 1) // capacity
