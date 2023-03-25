class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        
        visited = [0]*n
        
        h_map = {}
        
        for i,j in edges:
            if i not in h_map:
                h_map[i]=set()
            if j not in h_map:
                h_map[j]=set()
            h_map[i].add(j)
            h_map[j].add(i)
        
        def dfs(val):
            c = 1
            if visited[val]:
                return 0
            visited[val]=1
            if val in h_map:
                for new in h_map[val]:
                    c+=dfs(new)
            return c
        
        total = 0
        old_c = 0
        for i in range(n):
            val = dfs(i)
            if old_c ==0:
                old_c=val
                continue
            if val:
                total+=old_c*val
                old_c+=val
        return total
                
            