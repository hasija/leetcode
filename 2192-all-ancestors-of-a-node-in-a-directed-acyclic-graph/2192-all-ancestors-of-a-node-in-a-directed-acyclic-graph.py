class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for i,j in edges:
            graph[j].add(i)
        
        @lru_cache
        def dfs(v):
            ans = graph[v].copy()
            for u in graph[v]:
                ans.update(dfs(u))
            return ans
        final = []
        for i in range(n):
            final.append(sorted(list(dfs(i))))
        return final