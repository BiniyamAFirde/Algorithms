class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Initialize visited matrices for both oceans
        pacific_visited = [[False] * n for _ in range(m)]
        atlantic_visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y, visited):
            """DFS to mark all cells that can flow to the ocean"""
            visited[x][y] = True
            
            # Check all four directions
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                # Check bounds and if not visited and can flow backwards
                if (0 <= nx < m and 0 <= ny < n and 
                    not visited[nx][ny] and heights[nx][ny] >= heights[x][y]):
                    dfs(nx, ny, visited)
        
        # Start DFS from Pacific Ocean edges
        for i in range(m):
            dfs(i, 0, pacific_visited)  # left column
        for j in range(n):
            dfs(0, j, pacific_visited)  # top row
        
        # Start DFS from Atlantic Ocean edges
        for i in range(m):
            dfs(i, n - 1, atlantic_visited)  # right column
        for j in range(n):
            dfs(m - 1, j, atlantic_visited)  # bottom row
        
        # Find cells that can flow to both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])
        
        return result
