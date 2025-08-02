class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic={}
        result=[]
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i,j in dic.items():
            if j==1:
                result.append(i)
        return result
