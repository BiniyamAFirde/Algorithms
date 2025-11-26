class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_num = max(nums)
        points = [0] * (max_num + 1)
        
        for num in nums:
            points[num] += num
        
        # Space optimized DP
        prev2, prev1 = 0, points[1]
        
        for i in range(2, max_num + 1):
            current = max(prev1, points[i] + prev2)
            prev2, prev1 = prev1, current
        
        return prev1
