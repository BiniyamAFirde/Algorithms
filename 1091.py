from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
      
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
       
        if n == 1:
            return 1
      
        directions = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1)]
     
        distance = [[-1] * n for _ in range(n)]
        distance[0][0] = 1
        
        queue = deque([(0, 0)])
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < n and 0 <= new_col < n and 
                    grid[new_row][new_col] == 0 and distance[new_row][new_col] == -1):
                    
                    distance[new_row][new_col] = distance[row][col] + 1
                    
                    # Early termination if we reach destination
                    if new_row == n-1 and new_col == n-1:
                        return distance[new_row][new_col]
                    
                    queue.append((new_row, new_col))
        
        return distance[n-1][n-1] if distance[n-1][n-1] != -1 else -1
