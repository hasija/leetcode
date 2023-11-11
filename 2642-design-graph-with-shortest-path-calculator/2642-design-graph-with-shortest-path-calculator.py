class Graph:

    
    def short_path(self, n1, n2):
        visited = set()
       
                    
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for l,r,c in edges:
            self.graph[l].append((r,c))


    def addEdge(self, edge: List[int]) -> None:
        l,r,c = edge
        self.graph[l].append((r,c))

    def shortestPath(self, n1: int, n2: int) -> int:

        cost_map = {}
        cost_map[n1]=0
        max_c = float(inf)
        trace = [(0, n1)]
        while trace:
            edge = heapq.heappop(trace)
            cost, n = edge
            if n == n2:
                continue
            for edge in self.graph[n]:
                r,c = edge
                if r in cost_map and (c+cost< cost_map[r]):
                    cost_map[r]=c+cost
                    heapq.heappush(trace, (c+cost, r))
                elif r not in cost_map:
                    cost_map[r]=c+cost
                    heapq.heappush(trace, (c+cost, r))
        return cost_map[n2] if n2 in cost_map else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)