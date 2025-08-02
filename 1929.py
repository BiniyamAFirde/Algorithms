class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new=[]
        new2=[]
        for i in range(len(nums)):
            new.append(nums[i])
            new2.append(nums[i])
        return new+new2
