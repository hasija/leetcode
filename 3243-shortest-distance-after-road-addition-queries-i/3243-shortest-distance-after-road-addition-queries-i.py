

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        hmap = defaultdict(set)
        for i in range(n):
            if i!=n-1:
                hmap[i].add(i+1)


        def add_path(u,v):
            hmap[u].add(v)
        
        def bfs():
            queue = deque([0])
            ans = 0
            visited = set()
            while True:
                new_queue = deque()
                while queue:
                    node = queue.popleft()
                    for new_node in hmap[node]:
                        if new_node in visited:
                            continue
                        new_queue.append(new_node)
                        visited.add(new_node)
                        if new_node==n-1:
                            return ans+1
                ans+=1
                if new_queue:
                    queue = new_queue
                else:
                    return n-1
            
        out = []
        for u,v in queries:
            add_path(u,v)
            out.append(bfs())
        return out
            