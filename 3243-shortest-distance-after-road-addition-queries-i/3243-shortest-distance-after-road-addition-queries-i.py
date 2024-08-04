class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        roads = defaultdict(list)
        curr_max = n-1
        ans = []
        for i in range(n-1):
            roads[i].append(i+1)

        def bfs():
            queue = deque([0])
            ans = 0
            visited = set()
            while True:
                # print ("start with queue", queue)
                new_queue = deque([])
                while queue:
                   
                    
                    idx = queue.popleft()
                    # print ("working on idx", idx)
                    if idx in visited:
                        # print ("already visited")
                        continue
                    visited.add(idx)
                    if idx == n-1:
                        # print ("match found", ans)
                        return ans
                    for new in roads[idx]:
                        # print ("new roads from ",idx, "to ", new)
                        new_queue.append(new)
                ans+=1
                queue = new_queue.copy()
                # print ("new_queue", new_queue)
                if len(new_queue)==0:
                    return -1
            


        for i,j in queries:
            # print ("adding new road", i, j)
            roads[i].append(j)
            ans.append(bfs())
        return ans
        