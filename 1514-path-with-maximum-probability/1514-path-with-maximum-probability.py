class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            u,v  = edges[i]
            adj[u].append([v, succProb[i]])
            adj[v].append([u, succProb[i]])
        
        pq = [(-1, start)]
        
        visit = set()
        
        while pq:
            prob, node = heapq.heappop(pq)
            if node ==end:
                return prob*-1
            if node not in visit:
                visit.add(node)
                for n in adj[node]:
                    v,p = n
                    heapq.heappush(pq, (p*prob, v))
                
            
        return 0