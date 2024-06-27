class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}
        for u,v in edges:
            
            
            if u in graph:
                return u
            graph[u]=v
            if v in graph:
                return v
            graph[v] = u

        
        