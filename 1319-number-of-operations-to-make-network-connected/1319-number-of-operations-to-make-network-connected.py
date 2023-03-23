import heapq
class Solution:
    def makeConnected(self, n, connections):
        if len(connections)<n-1:
            return -1
        G = collections.defaultdict(set)
        for i,j in connections:
            G[i].add(j)
            G[j].add(i)
        
        seen = [0]*n
        def dfs(val):
            if seen[val]:
                return 0
            seen[val]=1
            for new in G[val]:
                dfs(new)
            return 1
        
        return sum([dfs(i) for i in range(n)]) -1
        