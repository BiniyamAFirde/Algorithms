class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''total=1
        zero_count=0
        zero_index=0

        for i,num in enumerate (nums):
            if num==0:
                zero_index= i
                zero_count+=1
            else:
                total*=num
        result=[]
        for i,num  in enumerate(nums):
            if zero_count>1:
                result.append(0)
            elif zero_count==1:
                if num==0:
                    result.append(total)
                else:
                    result.append(0)
            else:
                result.append(total//num)
        return result
'''
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

        """
    "Left pass captures "everything before me"

    "Right pass captures "everything after me"

    "Combining them gives "everything except me"

    The beauty is that by separating left and right, we never multiply by the   element at the current position, which is exactly what "product except self" requires."""
