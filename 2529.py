class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countp=0
        countn=0
        for i in range(len(nums)):
            if nums[i]<0:
                countp+=1
            elif nums[i]>0:
                countn+=1
        if countn > countp:
            return countn
        else:
            return countp
