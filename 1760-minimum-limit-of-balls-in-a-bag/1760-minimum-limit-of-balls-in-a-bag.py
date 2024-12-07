class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check_max(max_balls):
            local_sum = 0
            for i in nums:
                local_sum += ceil((i/max_balls)-1)
                if local_sum>maxOperations:
                    return False
            return True
        
        l = 1
        r = max(nums)
        ans = float('inf')
        while l<=r:
            mid = (l+r)//2
            if check_max(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
                
            