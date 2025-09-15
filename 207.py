from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Build the graph and in-degree array
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        # Initialize the queue with all nodes having in-degree 0
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses
