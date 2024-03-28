class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        cnt = defaultdict(int)
        ans = 0
        for ind, i in enumerate(nums):
            cnt[i]+=1
            while cnt[i]>k:
                cnt[nums[start]]-=1
                start+=1
            ans = max(ans, (ind-start+1))
        return ans
            
                