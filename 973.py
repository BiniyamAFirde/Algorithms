class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points_with_dist = [(x*x + y*y, [x, y]) for x, y in points]

        points_with_dist.sort(key=lambda x: x[0])
        
        result = [point for dist, point in points_with_dist[:k]]
        
        return result
