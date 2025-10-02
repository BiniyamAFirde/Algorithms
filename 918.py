class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = max_so_far = nums[0]
        current_min = min_so_far = nums[0]
        total_sum = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
            
            current_min = min(nums[i], current_min + nums[i])
            min_so_far = min(min_so_far, current_min)
            
            total_sum += nums[i]

        if max_so_far < 0:
            return max_so_far

        return max(max_so_far, total_sum - min_so_far)
