class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            grid[i][j] = 0  # mark as visited
            area = 1
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    if current_area > max_area:
                        max_area = current_area
        return max_area
