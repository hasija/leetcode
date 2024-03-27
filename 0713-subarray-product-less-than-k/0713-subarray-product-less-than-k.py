class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        num_cnt = 0
        prod = 1
        ans = 0
        start = 0
        if k ==0 or k==1:
            return 0
        for ind, i in enumerate(nums):
            prod = prod*i
            num_cnt+=1
            if prod<k:
                ans+=num_cnt
            else:
                while prod>=k:
                    prod/=nums[start]
                    start+=1
                    num_cnt-=1
                ans+=num_cnt
            # print ("ans", ans, "count", num_cnt, "prod", prod, 'start', start)
        return ans
                