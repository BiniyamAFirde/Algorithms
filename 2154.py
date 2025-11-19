class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in nums:
            if i == nums or original in nums:
                original*=2
            else:
                return original
        return original
