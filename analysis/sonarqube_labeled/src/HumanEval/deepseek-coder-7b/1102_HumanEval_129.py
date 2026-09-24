
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    visited = set()
    min_path = []

    for i in range(n):
        for j in range(n):
            queue.append(((i, j), [grid[i][j]], [(i, j)]))

    while queue:
        (x, y), path, visited_path = queue.popleft()

        if len(path) == k + 1:
            if not min_path or path < min_path:
                min_path = path
        else:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited_path:
                    new_path = path + [grid[nx][ny]]
                    new_visited_path = visited_path + [(nx, ny)]
                    queue.append(((nx, ny), new_path, new_visited_path))
                    visited.add((nx, ny))

    return min_path[1:]
