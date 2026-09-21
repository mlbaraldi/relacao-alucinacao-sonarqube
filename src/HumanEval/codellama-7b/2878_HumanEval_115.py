
def max_fill(grid, capacity):
    import math
    # Initialize the number of times we need to lower the buckets
    num_lowers = 0

    # Loop through each row of the grid
    for row in grid:
        # Initialize the number of units of water in the current row
        num_units = 0

        # Loop through each well in the current row
        for well in row:
            # If the well is filled with water, add its capacity to the total
            if well == 1:
                num_units += capacity

        # If the total number of units of water in the current row is greater than the capacity,
        # we need to lower the buckets in that row
        if num_units > capacity:
            num_lowers += 1

    return num_lowers
