from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        queue = deque()
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # Directions for adjacent cells (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        
        # BFS starting from initially rotten oranges
        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
        
        return minutes if fresh_count == 0 else -1
