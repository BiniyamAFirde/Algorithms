from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Queue for BFS
        q = deque()
        
        # Add all border 'O's to the queue
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][n-1] == 'O':
                q.append((i, n-1))
                
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[m-1][j] == 'O':
                q.append((m-1, j))
                
        # Mark all border-connected 'O's as 'T'
        while q:
            x, y = q.popleft()
            board[x][y] = 'T'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = 'T'  # Mark immediately to avoid duplicates
                    q.append((nx, ny))
                    
        # Replace all 'T's with 'O', and the remaining 'O's with 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
