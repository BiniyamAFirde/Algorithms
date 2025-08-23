class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, cursets = [], []
        self.helper(0, nums, subsets, cursets)
        return subsets
    
    def helper(self, i, nums, subsets, cursets):
        if i >= len(nums):
            subsets.append(cursets.copy())
            return
        
        # Include current element
        cursets.append(nums[i])
        self.helper(i + 1, nums, subsets, cursets)
        cursets.pop()
        
        # Exclude current element
        self.helper(i + 1, nums, subsets, cursets)
