class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
        """
        result = []
        for i in nums:
            if i in result: 
                return True
            result.append(i)
        return False
        """
        
