import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = [[efficiency[i],speed[i]] for i in range(n)]
        arr = sorted(arr, key = lambda x: -x[0])
        # print(arr)
        max_s = []
        max_p = 0
        max_sum = 0
        for i in range(n):
            # if i<k-1:
            #     heapq.heappush(max_s, arr[i][-1])
            #     continue
            perform = (max_sum+arr[i][-1])*arr[i][0]
            if perform>max_p:
                max_p = perform
            if len(max_s)>=k-1 and len(max_s)>=1 and max_s[0]<arr[i][-1]:
                max_sum-=max_s[0]
                max_sum+=arr[i][-1]
                heapq.heappushpop(max_s, arr[i][-1])
            elif len(max_s)<k-1:
                max_sum+=arr[i][-1]
                heapq.heappush(max_s, arr[i][-1])
            # print (max_s)
        return max_p%(10**9+7)