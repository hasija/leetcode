class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        uf = [i for i in range(n)]
        
        direct_map = collections.defaultdict(set)
        
        for i,j in edges:
            direct_map[i].add(j)
        
        
        def dfs(v, head):
            if uf[v]!=v:
                return uf[v]
            uf[v]=head
            
            for out in direct_map[v]:
                dfs(out, v)
        
        out = []
        
        for i in range(n):
            dfs(i,i)
            # print (uf)
        for i in range(n):
            if uf[i]==i:
                out.append(i)
        return out
        