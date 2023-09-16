class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        
        dist = [[float('inf')]*cols for i in range(rows)]
        heap = [(0,0,0)]
        
        delta_r = [0,0,1,-1]
        delta_c = [1,-1,0,0]
        delta = list(zip(delta_r,delta_c))
        while heap:
            d,r,c = heapq.heappop(heap)
            if r==rows-1 and c==cols-1:
                return d
            for dr, dc in delta:
                nr = dr+r
                nc = dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    new_dist = max(abs(heights[r][c]-heights[nr][nc]), d)
                    if new_dist<dist[nr][nc]:
                        dist[nr][nc]=new_dist
                        heapq.heappush(heap, (new_dist,nr,nc))