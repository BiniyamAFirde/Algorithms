class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)): 
            key=nums[i]
            j=i
            while j>0 and nums[j-1]>key:
                nums[j]=nums[j-1]
                j-=1
                nums[j]=key
