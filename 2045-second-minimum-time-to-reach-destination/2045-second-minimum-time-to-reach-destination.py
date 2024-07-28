class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        
        def dijkstra(s, graph):
            visited = set()
            flag = False
            queue = [(0, s)]
            shortest_path = [float('inf')]*(n+1)
            shortest_path_2 = [float('inf')]*(n+1)
            shortest_path[s]=0
            while queue:
                walk, node = heapq.heappop(queue)
                if shortest_path_2[n]!=float('inf'):
                    new_time = shortest_path_2[n]
                    return new_time
                
                for nxt_node in graph[node]:
                    dist = time
                    if shortest_path_2[nxt_node]!=float('inf'):
                        continue
                        
                    if (walk//change)%2!=0:
                        new_time = change-(walk%change)+walk+time
                    else:
                        new_time = walk+dist
                    if new_time<shortest_path[nxt_node]:
                        shortest_path_2[nxt_node] = shortest_path[nxt_node]
                        shortest_path[nxt_node] = new_time
                        heapq.heappush(queue, (new_time, nxt_node))
                    elif ( shortest_path_2[nxt_node]>new_time and shortest_path[nxt_node]!=new_time):
                        shortest_path_2[nxt_node] = new_time
                        heapq.heappush(queue, (new_time, nxt_node))
                        
                
            return shortest_path_2
        return dijkstra(1, graph)
