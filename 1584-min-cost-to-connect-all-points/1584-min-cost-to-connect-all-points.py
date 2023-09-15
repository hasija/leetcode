class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_cost(p1, p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

        cost = defaultdict(list)
        for ind,p1 in enumerate(points):
            for ind2, p2 in enumerate(points):
                if ind2<=ind:
                    continue
                c = get_cost(p1, p2)
                cost[ind].append((c,ind2))
                cost[ind2].append((c,ind))
        
        n = len(points)
        visited = [0]*n
        visited[0] = 1
        heap = cost[0]
        heapq.heapify(heap)
        # print (heap)
        cnt = 1
        ans = 0
        while cnt<n and len(heap)>0:
            d,ind = heapq.heappop(heap)
            if visited[ind]!=1:
                ans+=d
                visited[ind]=1
                cnt+=1
                # print (ans, d, ind)
                for val in cost[ind]:
                    heapq.heappush(heap,val)
        
        return ans
            
        
                
                
                
            
        