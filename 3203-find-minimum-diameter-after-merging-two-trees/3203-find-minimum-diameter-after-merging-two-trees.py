class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        hmap = defaultdict(list)
        
        
        def bfs(graph, edge):
            bfs = [edge]
            seen = set()
            diameter = 0
            last_val = edge
            while True:
                next_arr = set()
                for node in bfs:
                    last_val = node
                    seen.add(node)
                    for next_node in graph[node]:
                        if next_node not in seen:
                            next_arr.add(next_node)
                bfs = next_arr
                if not bfs:
                    return diameter, last_val
                diameter+=1
            
            
        
        
        
        for i,j in edges1:
            hmap[i].append(j)
            hmap[j].append(i)
        
        _, edge = bfs(hmap, 0)
        d1, _ = bfs(hmap, edge)
        
        
        
        hmap2 = defaultdict(list)
        for i,j in edges2:
            hmap2[i].append(j)
            hmap2[j].append(i)
        
        _, edge = bfs(hmap2, 0)
        d2, _ = bfs(hmap2, edge)
        
        # print(d1, d2)
        
        return max(ceil(d1/2)+ceil(d2/2)+1,d1,d2)
        
            
        
        