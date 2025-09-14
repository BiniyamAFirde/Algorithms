class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        # Initialize the queue with all land cells and set their distance to 0.
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # If there are no land cells or all cells are land, return -1.
        if not q or len(q) == n * n:
            return -1
        
        max_dist = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    max_dist = max(max_dist, dist[nx][ny])
                    q.append((nx, ny))
        
        return max_dist
