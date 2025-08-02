class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for r in nums:
            if r in dic:
                dic[r]+=1
            else:
                dic[r]=1
        for r,count in dic.items():
            if count==1:
                return r
        return -1
