class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # Helper function to solve the linear house robber problem
        def rob_linear(arr):
            n_arr = len(arr)
            if n_arr == 0:
                return 0
            if n_arr == 1:
                return arr[0]
            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])
            for i in range(2, n_arr):
                current = max(arr[i] + prev2, prev1)
                prev2 = prev1
                prev1 = current
            return prev1
        
        # Scenario 1: Exclude the last house (rob houses 0 to n-2)
        scenario1 = rob_linear(nums[:-1])
        # Scenario 2: Exclude the first house (rob houses 1 to n-1)
        scenario2 = rob_linear(nums[1:])
        
        return max(scenario1, scenario2)
      
