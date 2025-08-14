'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
       
        a=0
        nam=list(set(nums))
        for i in range(len(nam)):
            highmax=nam[i]
            for i in range(1,len(nam)):
                if nam[i]>highmax:
                    highmax=nam[i]
                    a+=1
        if a>=3:
            return min(nam)
        else:
            return highmax  
        '''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -float('inf')
        
        for num in set(nums):
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        return third if third != -float('inf') else first




        
