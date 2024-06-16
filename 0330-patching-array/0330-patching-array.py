class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        idx = 0
        ans = 0
        LEN = len(nums)
        while miss<=n:
            if idx<LEN and nums[idx]<=miss:
                miss+=nums[idx]
                idx+=1
            else:
                miss+=miss
                ans+=1
        return ans
            
            