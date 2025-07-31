class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result=[]
        odd=[]
        for r in range(len(nums)):
            if nums[r]%2==0:
                result.append(nums[r])
            else:
                odd.append(nums[r])
        return result+odd
