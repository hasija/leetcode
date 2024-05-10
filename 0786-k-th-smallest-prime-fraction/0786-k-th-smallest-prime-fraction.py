class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        len_ = len(arr)
        MIN = float('inf')
        ans = []
        for i in range(len_):
            for j in range(i+1,len_):
                diff = arr[i]/arr[j]
                heapq.heappush(ans,(diff, (i,j)))
        cnt = 1
        while cnt!=k:
            heapq.heappop(ans)
            cnt+=1
        i,j = ans[0][1]
        return [arr[i], arr[j]]