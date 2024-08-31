class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)    
        for idx, edge in enumerate(edges):
            u,v = edge
            prob = succProb[idx] 
            graph[u].append((v,prob))
            graph[v].append((u,prob))
            
        def shortest_path(start):
            max_prob = [0]*n
            max_prob[start]=1
            heap = [(-1, start)]
            visited = set()
            while heap:
                prob, node = heapq.heappop(heap)
                visited.add(node)
                for v,nxt_prob in graph[node]:
                    if v not in visited and max_prob[v]<-prob*nxt_prob:
                        max_prob[v] = -prob*nxt_prob
                        heapq.heappush(heap, (prob*nxt_prob, v))
            print(max_prob)
            return max_prob[end_node]
        return shortest_path(start_node)
                        
                    