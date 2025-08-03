class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for num in operations:
            if num.lstrip('-').isdigit():  
                result.append(int(num))
            elif num == "+":
                result.append(result[-1] + result[-2])
            elif num == "D":
                result.append(2 * result[-1])
            elif num == "C":
                result.pop()
        return sum(result)
