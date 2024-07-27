class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        graph = [[float('inf')]*26 for i in range(26)]
        for idx,i in enumerate(original):
            l=ord(i)-97
            r=ord(changed[idx])-97
            val = cost[idx]
            if graph[l][r]>val:
                graph[l][r]=val
        
        def dijkstra(s, graph):
            p_queue = [(0,s)]
            visited = set()
            shortest_dist = [float(inf)]*26
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
        def dijkstra2(s, graph):
            visited = set()
            queue = [(0,s)]
            shortest_path = [float('inf')]*26
            shortest_path[s]=0
            while queue:
                curr_walk, node = heapq.heappop(queue)
                # if node not in visited:
                #     visited.add(node)
                # else:
                #     continue
                for idx, nxt_val in enumerate(graph[node]):
                    if nxt_val+curr_walk<shortest_path[idx]:
                        shortest_path[idx]=nxt_val+curr_walk
                        heapq.heappush(queue, (nxt_val+curr_walk, idx))
            return shortest_path
       
        all_paths = []
        for i in range(26):
            all_paths.append(dijkstra(i, graph.copy()))
        ans = 0
        # for i in all_paths:
        #     print (i)
        for idx in range(len(source)):
            s = source[idx]
            t = target[idx]
            if s!=t:
                s_idx = ord(s)-97
                t_idx = ord(t)-97
                curr = all_paths[s_idx][t_idx]
                if curr==float('inf'):
                    return -1
                else:
                    ans+=curr
        return ans
        
        
        
        
        
        
        
        
        