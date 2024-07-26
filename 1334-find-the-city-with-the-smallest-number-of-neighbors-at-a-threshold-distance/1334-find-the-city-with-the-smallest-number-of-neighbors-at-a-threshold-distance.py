class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float(inf)]*n for i in range(n)]
        for i,j,w in edges:
            graph[i][j]=graph[j][i]=w
        
        all_paths = []
        def dijkstra(s, graph):
            p_queue = [(0,s)]
            visited = set()
            shortest_dist = [float(inf)]*n
            shortest_dist[s]=0
            while p_queue:
                curr_walk, curr_node = heapq.heappop(p_queue)
                if curr_node not in visited:
                    visited.add(curr_node)
                else:
                    continue
                for node, i in enumerate(graph[curr_node]):
                    if i+curr_walk<shortest_dist[node]:
                        shortest_dist[node] = i+curr_walk
                        heapq.heappush(p_queue, (i+curr_walk, node))
                    else:
                        continue
            return shortest_dist
        for i in range(n):
            all_paths.append(dijkstra(i, graph.copy()))
        
        
        min_cnt = float('inf')
        min_city = None
        for city, paths in enumerate(all_paths):
            local_cnt = sum([1 for path in paths if path<=distanceThreshold])
            if local_cnt<min_cnt:
                min_city = city
                min_cnt = local_cnt
            elif local_cnt==min_cnt:
                min_city = city
        return min_city
                    
                
    
    
    
    
    
    
    
    