class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        
        for num in nums:
            digit_count = 0
            x = num

            # count digits
            while x > 0:
                x //= 10
                digit_count += 1
            
            # check even
            if digit_count % 2 == 0:
                even_count += 1
        
        return even_count
