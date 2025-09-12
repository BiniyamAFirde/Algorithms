from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        total_rows = len(wall)
        for row in wall:
            current_width = 0
            for brick in row[:-1]:  
                current_width += brick
                edge_count[current_width] += 1
        
        max_edges = max(edge_count.values()) if edge_count else 0
        return total_rows - max_edges
