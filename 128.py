class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Check if this is the start of a sequence
            # (num-1 not in set means it's a starter)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Expand the sequence as long as we can
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
        
