class Solution:
    def reverse(self, x: int) -> int:
        # Handle sign
        is_negative = x < 0
        x_str = str(abs(x))
        
        # Build reversed string by iterating from the end
        reversed_str = ""
        for i in range(len(x_str)-1, -1, -1):
            reversed_str += x_str[i]
        
        # Convert back to integer
        reversed_num = int(reversed_str)
        
        # Apply sign
        if is_negative:
            reversed_num = -reversed_num
        
        # Check for 32-bit integer overflow
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num
        
