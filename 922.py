class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_ptr = 0  # pointer for even positions
        odd_ptr = 1   # pointer for odd positions
        
        while even_ptr < len(nums) and odd_ptr < len(nums):
            # If even position has odd number and odd position has even number, swap them
            if nums[even_ptr] % 2 == 1 and nums[odd_ptr] % 2 == 0:
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
                even_ptr += 2
                odd_ptr += 2
            # If even position has even number, move to next even position
            elif nums[even_ptr] % 2 == 0:
                even_ptr += 2
            # If odd position has odd number, move to next odd position
            else:
                odd_ptr += 2
        
        return nums
