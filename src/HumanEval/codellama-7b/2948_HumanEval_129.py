
def minPath(grid, k):
    # Initialize the table of values
    values = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Set the starting cell to 0
    values[0][0] = 0

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell is not the starting cell, check if it is on the path
            if i != 0 or j != 0:
                # Calculate the minimum path length from the starting cell to this cell
                min_path_length = min(values[i-1][j], values[i][j-1], values[i-1][j-1])

                # Update the table of values
                values[i][j] = min_path_length + 1

    # Find the minimum path length from the starting cell to the ending cell
    min_path_length = values[len(grid)-1][len(grid[0])-1]

    # Return the ordered list of values on the cells that the minimum path goes through
    return [grid[i][j] for i, j in zip(range(len(grid)), range(len(grid[0])))]
