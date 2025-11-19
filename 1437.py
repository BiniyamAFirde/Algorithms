class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        seen_first_one = False
        count = 0

        for num in nums:
            if num == 1:
                if seen_first_one and count < k:
                    return False
                seen_first_one = True
                count = 0
            else:
                if seen_first_one:
                    count += 1

        return True
