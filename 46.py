class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.helper(nums, [], permutations)
        return permutations
    
    def helper(self, nums, current, permutations):
        if len(nums) == 0:
            permutations.append(current.copy())
            return
        
        for i in range(len(nums)):
            # Choose current element
            current.append(nums[i])
            remaining = nums[:i] + nums[i+1:]
            
            # Recurse with remaining elements
            self.helper(remaining, current, permutations)
            
            # Backtrack
            current.pop()
