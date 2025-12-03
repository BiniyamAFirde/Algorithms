class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        foundword=False
        for i in range(len(s)-1,-1,-1):
            
            if  s[i]!=" ":
                count+=1
                foundword=True
            elif foundword:
                break
        return count
