class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        arr = deque([(1<<i,i,0) for i in range(n)])
        visited = set([(1<<i,i) for i in range(n)])
        final_mask = (1<<n) -1
        while arr:
            mask, node, dist = arr.popleft()
            if mask == final_mask:
                return dist
            for nxt in graph[node]:
                new_mask = mask|1<<nxt
                if (new_mask,nxt) in visited:
                    continue
                nxt_set = (new_mask, nxt, dist+1)
                nxt_visit = (new_mask,nxt)
                arr.append(nxt_set)
                visited.add(nxt_visit)