class Solution:
    def isValid(self, s: str) -> bool:
        """s=list(s)
        result=[]
        for i in range(len(s)):
            if s[i]=="(" and s[i+1]=="]":
                return False
            elif s[i]=="[" and s[i+1]==")":
                return False
            elif s[i]=="{" and s[i+1]==")":
                return False
            elif s[i]=="(" and s[i+1]=="}":
                return False
            elif s[i]=="[" and s[i+1]=="}":
                return False
            elif s[i]=="{" and s[i+1]=="]":
                return False
            
        return True"""
        result = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for i in s:
            if i in mapping: 
                top_element = result.pop() if result else '#'
                if mapping[i] != top_element:
                    return False
            else:  
                result.append(i)
        return not result
