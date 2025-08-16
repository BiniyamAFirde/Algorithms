class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if target in matrix[j]:
                    return True
        return False
        
