class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
        def get_shortest_path(edges):

            
            # def get_min_val(visited, shortest_path):
            #     dist = float('inf')
            #     node = None
            #     for i in range(n):
            #         if i not in visited and shortest_path[i]<dist:
            #             dist = shortest_path[i]
            #             node = i
            #     return node
                    
            
            def dijkstra(source):
                shortest_path = [float('inf')]*n
                shortest_path[source]=0
                
                heap = [(0, source)]
                while heap:
                    dist, node = heapq.heappop(heap)
                    for v,w in graph[node]:
                        if v==node:
                            continue
                        if shortest_path[v]>shortest_path[node]+w:
                            heapq.heappush(heap,(shortest_path[node]+w, v))
                            shortest_path[v]=shortest_path[node]+w

                return shortest_path[destination]                
                    

            return dijkstra(source)
            # print (shortest_path)
            
        
        graph = [[] for i in range(n)]

            
        for u,v,w in edges:
            if w!=-1:
                graph[u].append((v,w))
                graph[v].append((u,w))

        dist = get_shortest_path(edges)
        # print (dist)
        flag = False
        if dist == target:
            flag = True
        if dist<target:
            return []
            
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if flag and edge[2]==-1:
                edge[2]= 2 * (10**9)
                continue
            elif edge[2]==-1:
                edge[2]=1
                graph[u].append((v, edge[2]))
                graph[v].append((u, edge[2]))
            else:
                continue
            
            dist = get_shortest_path(edges)
            # print ("dist in loop", dist)
            if dist <= target:
                edge[2]+=target-dist
                flag = True
        if flag:
            return edges
        else:
            return []
                
                
            
            