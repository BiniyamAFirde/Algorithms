class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        
        s1 = set(nums1)
        s2 = set(nums2)
        common = s1 & s2
        n = len(nums1)
        
        unique1 = len(s1 - common)
        unique2 = len(s2 - common)
        common_count = len(common)
        
      
        take_unique1 = min(unique1, n // 2)
        take_unique2 = min(unique2, n // 2)
        
      
        remaining_slots1 = max(0, n // 2 - take_unique1)
        remaining_slots2 = max(0, n // 2 - take_unique2)
        
        
        take_common = min(common_count, remaining_slots1 + remaining_slots2)
        
        return take_unique1 + take_unique2 + take_common
