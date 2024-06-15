class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pro_cap = list(zip(profits,capital))
        pro_cap = [(-i,j) for i,j in pro_cap]
        heapq.heapify(pro_cap)
        while k>0:
            
            arr = []
            while pro_cap and pro_cap[0][1]>w :
                arr.append(heapq.heappop(pro_cap))
            if len(pro_cap)==0:
                return w
            # print (pro_cap[0][0])
            w+=-1*pro_cap[0][0]
            k-=1
            heapq.heappop(pro_cap)
            for i in arr:
                heapq.heappush(pro_cap, i)

        return w
        
        
        