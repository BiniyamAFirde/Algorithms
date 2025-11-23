class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([0])  # Start index
        visited = set()
        
        while queue:
            start = queue.popleft()
            
            if start == len(s):
                return True
                
            if start in visited:
                continue
                
            visited.add(start)
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    queue.append(end)
        
        return False
