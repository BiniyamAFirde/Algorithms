class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add=0
        result=[]
        for i in range(len(nums)):
            add+=nums[i]
            result.append(add)
        return result
