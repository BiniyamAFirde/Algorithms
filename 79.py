class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]):
                return False
            if k == len(word) - 1:
                return True
            temp = board[i][j]
            board[i][j] = '#'  # mark as visited
            found = (dfs(i+1, j, k+1) or
                    dfs(i-1, j, k+1) or
                    dfs(i, j+1, k+1) or
                    dfs(i, j-1, k+1))
            board[i][j] = temp  # revert back
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
