class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26  
        left = 0
        max_length = 0
        max_freq = 0
        
        for right in range(len(s)):
 
            idx = ord(s[right]) - ord('A')
            char_count[idx] += 1

            max_freq = max(max_freq, char_count[idx])

            if (right - left + 1) - max_freq > k:
                left_idx = ord(s[left]) - ord('A')
                char_count[left_idx] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
