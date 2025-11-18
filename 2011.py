class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in range(len(operations)):
            if operations[i] == "X--"or operations[i] == "--X":
                operations[i]=-1
            if operations[i] == "X++"or operations[i] == "++X":
                operations[i]=1
            x+=operations[i]
        return x
