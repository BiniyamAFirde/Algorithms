class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_dict = {}
        for index, num in enumerate(nums):
            needed_num = target - num
            if needed_num in num_dict:
                return [num_dict[needed_num], index]
            num_dict[num] = index
        return []
