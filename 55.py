class Solution:
    @staticmethod
    def canJump(nums):
        """
        Determine if you can reach the last index starting from the first index.
        
        Args:
            nums: List of integers representing maximum jump length at each position
        
        Returns:
            bool: True if last index is reachable, False otherwise
        """
        farthest = 0  # Farthest position we can reach
        
        for i in range(len(nums)):
            # If current position is beyond what we can reach, return false
            if i > farthest:
                return False
            
            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or go beyond the last index, return true
            if farthest >= len(nums) - 1:
                return True
        
        return False
            
