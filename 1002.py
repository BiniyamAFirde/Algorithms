
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the common frequency with the first word
        common_freq = Counter(words[0])
        
        # Iterate through the rest of the words
        for word in words[1:]:
            current_freq = Counter(word)
            # Update common_freq to keep the minimum count for each character
            for char in common_freq:
                if char in current_freq:
                    common_freq[char] = min(common_freq[char], current_freq[char])
                else:
                    common_freq[char] = 0
        
        # Build the result list
        result = []
        for char, count in common_freq.items():
            result.extend([char] * count)
        
        return result
