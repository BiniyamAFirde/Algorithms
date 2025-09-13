from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        
        m, n = len(mat), len(mat[0])
        result = [[-1] * n for _ in range(m)]
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
       
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            i, j = queue.popleft()
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
            
                if 0 <= ni < m and 0 <= nj < n and result[ni][nj] == -1:
                    result[ni][nj] = result[i][j] + 1
                    queue.append((ni, nj))
        
        return result
        
