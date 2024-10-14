class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        # print(nums)
        heapq.heapify(nums)
        ans = 0
        
        for i in range(k):
            val = heapq.heappop(nums)
            val*=-1
            ans+=val
            push_val = ceil(val/3)
            heapq.heappush(nums, -push_val)
        return ans