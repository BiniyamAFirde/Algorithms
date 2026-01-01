class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2  # Avoids potential overflow
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is at mid or before mid
                right = mid
            else:
                # If mid is good, the first bad version must be after mid
                left = mid + 1
        
        # When left == right, we've found the first bad version
        return left
