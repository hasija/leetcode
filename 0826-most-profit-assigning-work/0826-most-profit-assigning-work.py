class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pro_diff = list(zip(difficulty, profit))
        pro_diff = sorted(pro_diff, key=lambda x: (x[0],-x[1]))
        worker.sort()
        ans = 0
        h_arr = []
        idx = 0
        for i in worker:
            while idx<len(pro_diff) and pro_diff[idx][0]<=i:
                heapq.heappush(h_arr, -pro_diff[idx][1])
                idx+=1
            if h_arr:
                ans-=h_arr[0]
        return ans