class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        new_arr = []
        for x1,x2,h in buildings:
            new_arr.append((x1,x2,-h))
            new_arr.append((x2,0,0))
            
        new_arr = sorted(new_arr, key = lambda x: (x[0], x[2], x[1]) )

        out = [[0,0]]
        
        max_heap = [[0, float('inf')]]
 
        for s,e,h in new_arr:
            # print ("start",x,h,p)
            while max_heap and max_heap[0][-1]<=s:
                heapq.heappop(max_heap)
            
            if h!=0:
                heapq.heappush(max_heap, [h, e])
            
            if out[-1][1]!=-max_heap[0][0]:
                out.append([s,-max_heap[0][0]])
        return out[1:]
            
            

        
        
        