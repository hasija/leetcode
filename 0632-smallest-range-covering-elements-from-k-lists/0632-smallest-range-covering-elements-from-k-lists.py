class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        c_n = len(nums[0])
        pq = []
        _max = -float('inf')
        for i in range(n):
            heapq.heappush(pq, (nums[i][0],i,0))
            _max = max(_max , nums[i][0])
        
        ans = [-float('inf'), float('inf')]
        # print("LEn and c Len",n, c_n)
        while pq:
            min_val, chain, idx = heapq.heappop(pq)
            if _max-min_val<ans[1]-ans[0]:
                ans = [min_val, _max]
            if idx+1==len(nums[chain]):
                break
            new_v = nums[chain][idx+1]
            heapq.heappush(pq, (new_v, chain, idx+1))
            _max = max(new_v, _max)
        return ans
         