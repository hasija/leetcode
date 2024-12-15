class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        arr = []
        for i,j in classes:
            ratio = (i+1)/(j+1)
            old_ratio = i/j
            val = ratio-old_ratio
            heapq.heappush(arr, (-val, (i,j)))
        
        while extraStudents:
            extraStudents-=1
            r,vals = heapq.heappop(arr)
            n = vals[0]+1
            d = vals[1]+1
            old_ratio = n/d
            new_ratio = (n+1)/(d+1)
            # print(n,d)
            # print("new ratio", new_ratio)
            # print("old ratio", r)
            final = (new_ratio-old_ratio)
            heapq.heappush(arr, (-final, (n, d)))
        # print(arr)
        
        ans = 0
        for i in arr:
            ans+= (i[1][0]/i[1][1])
        return round(ans/len(arr),5)
    