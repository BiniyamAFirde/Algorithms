class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(current_combination.copy())
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # Include the current candidate
                current_combination.append(candidates[i])
                current_sum += candidates[i]
                
                # Recursively try with the same candidate (since we can reuse)
                backtrack(i, current_combination, current_sum)
                
                # Backtrack: remove the last candidate
                current_sum -= candidates[i]
                current_combination.pop()
        
        backtrack(0, [], 0)
        return result
