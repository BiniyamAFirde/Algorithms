class Solution:
    def toLowerCase(self, s: str) -> str:
        new=""
        for i in range(len(s)):
            new+=s[i].lower()
        return new
