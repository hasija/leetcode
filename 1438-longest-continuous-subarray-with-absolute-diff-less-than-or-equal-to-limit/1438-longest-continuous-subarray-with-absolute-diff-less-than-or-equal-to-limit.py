class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_h = []
        min_h = []
        removed = set()
        ans = 1
        left = 0
        for idx, i in enumerate(nums):
            heapq.heappush(min_h, (i,idx))
            heapq.heappush(max_h, (-i,idx))
            while max_h and max_h and abs(max_h[0][0]+min_h[0][0])>limit:
                left = min(min_h[0][1], max_h[0][1])+1 
                while min_h and min_h[0][1]<left:
                    heapq.heappop(min_h)
                while max_h and max_h[0][1]<left:
                    heapq.heappop(max_h)
            ans = max(ans, idx-left+1)
        return ans