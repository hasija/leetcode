class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = [-1]*n
        hmap = defaultdict(list)
        queue = []
        for idx, q in enumerate(queries):
            i, j = q
            if i==j:
                res[idx] = i
            elif heights[i]>heights[j] and i>j:
                res[idx] = i
            elif heights[i]<heights[j] and i<j:
                res[idx] = j
            else:
                hmap[max(i,j)].append((max(heights[i],heights[j]),idx))
        
        for idx, h in enumerate(heights):
            while queue and queue[0][0]<h:
                _,res_idx = heapq.heappop(queue)
                res[res_idx] = idx

            for query in hmap[idx]:
                heapq.heappush(queue, query)
        return res            