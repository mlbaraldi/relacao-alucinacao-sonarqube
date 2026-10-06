
def minPath(grid, k):
    n = len(grid)
    # Find the starting cell with the minimum value
    min_val = float('inf')
    start = (0, 0)
    for i in range(n):
        for j in range(n):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                start = (i, j)
    
    path = [min_val]
    current_i, current_j = start
    
    for _ in range(k - 1):
        neighbors = []
        # Check all four possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = current_i + dx
            y = current_j + dy
            if 0 <= x < n and 0 <= y < n:
                neighbors.append((grid[x][y], x, y))
        
        # Find the neighbor with the smallest value
        if neighbors:
            min_neighbor = min(neighbors, key=lambda t: t[0])
            path.append(min_neighbor[0])
            current_i, current_j = min_neighbor[1], min_neighbor[2]
    
    return path
