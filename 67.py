class Solution:
    def addBinary(self, a: str, b: str) -> str:
 
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        carry = 0
        result = []
        

        for i in range(max_len - 1, -1, -1):
   
            total = int(a[i]) + int(b[i]) + carry
            
            if total == 0:
                result.append('0')
                carry = 0
            elif total == 1:
                result.append('1')
                carry = 0
            elif total == 2:
                result.append('0')
                carry = 1
            elif total == 3:
                result.append('1')
                carry = 1
        
        # If there's a carry left, add it
        if carry:
            result.append('1')
        
        # Reverse the result and join as string
        return ''.join(result[::-1])
