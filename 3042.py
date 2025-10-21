class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) <= len(words[j]):

                    is_prefix = words[j].startswith(words[i])

                    is_suffix = words[j].endswith(words[i])
                    
                    if is_prefix and is_suffix:
                        count += 1
        return count
