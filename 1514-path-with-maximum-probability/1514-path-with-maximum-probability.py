class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, vals in enumerate(edges):
            u,v = vals
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))
        
        visited = set()
        min_dist = defaultdict(int)
        arr = [(-1,start_node)]
        while arr:
            prob, node = heapq.heappop(arr)
            if node in visited:
                continue
            visited.add(node)
            for nxt_node, nxt_prob in graph[node]:
                if -1*prob*nxt_prob>min_dist[nxt_node]:
                    min_dist[nxt_node]=-1*prob*nxt_prob
                    heapq.heappush(arr, (-min_dist[nxt_node],nxt_node))
        # print (min_dist)
        return min_dist[end_node]
            