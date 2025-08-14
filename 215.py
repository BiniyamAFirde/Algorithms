class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=0
        nam=sorted(nums,reverse=True)
        '''
        for i in range(len(nam)):
            highmax= nam[i]
            for i in range(1,len(nam)):
                if nam[i]>highmax:
                    highmax=nam[i]
                    a+=1
                    '''
        return nam[k-1]
        
