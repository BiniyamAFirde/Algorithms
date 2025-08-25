class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i in range(len(mat)):
            count = 0
            
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
                else:
                    break
            rows.append((count, i))
        
        # Sort the rows: first by the number of soldiers, then by the row index
        rows.sort(key=lambda x: (x[0], x[1]))
        
        # Extract the first k indices
        result = [row[1] for row in rows[:k]]
        return result
