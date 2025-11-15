class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        result = [[1]]  # Start with first row
        
        for i in range(1, numRows):
            row = [1]  # First element is always 1
            
            # Calculate middle elements
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            
            row.append(1)  # Last element is always 1
            result.append(row)
        
        return result
