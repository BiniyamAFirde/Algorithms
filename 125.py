# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True
        new=""
        for ch in s:
            if ch.isalnum()==True:
                new+=ch.lower()
        b=""
        for i in range(len(new)-1,-1,-1):
                b+=new[i]
        if b==new:
            return True
        return False
