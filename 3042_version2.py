class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        
        for i in range(n):
            str1 = words[i]
            len1 = len(str1)
            
            for j in range(i + 1, n):
                str2 = words[j]
                len2 = len(str2)
     
                if len1 > len2:
                    continue

                is_prefix = True
                for k in range(len1):
                    if str1[k] != str2[k]:
                        is_prefix = False
                        break
                is_suffix = True
                for k in range(len1):
                    if str1[k] != str2[len2 - len1 + k]:
                        is_suffix = False
                        break
                
                if is_prefix and is_suffix:
                    count += 1
        
        return count
