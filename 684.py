class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]
    
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
      
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False  
        
            parent[root_y] = root_x
            return True  

        for edge in edges:
            u, v = edge
         
            if not union(u, v):
                return edge
        
        return []  

if __name__ == "__main__":
    sol = Solution()

    edges1 = [[1,2],[1,3],[2,3]]
    print(f"Input: {edges1}")
    print(f"Output: {sol.findRedundantConnection(edges1)}") 
    
    print()
    edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(f"Input: {edges2}")
    print(f"Output: {sol.findRedundantConnection(edges2)}") 
