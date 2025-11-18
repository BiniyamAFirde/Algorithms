class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square all elements
        result = [num * num for num in nums]
        # Sort the squared values
        result.sort()
        return result
