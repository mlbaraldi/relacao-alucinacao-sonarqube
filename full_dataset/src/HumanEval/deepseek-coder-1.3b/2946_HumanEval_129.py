
def minPath(grid, k):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    min_path = [float('inf')]*k
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y, path):
        nonlocal min_path
        path.append(grid[x][y])
        if len(path) == k:
            min_path = min(min_path, sorted(path))
            path.pop()
            return
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                dfs(nx, ny, path)
        visited[x][y] = False
        path.pop()

    for i in range(n):
        for j in range(n):
            dfs(i, j, [])

    return min_path
