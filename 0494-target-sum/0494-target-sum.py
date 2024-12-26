class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cnt = Counter()
        n = len(nums)
        def dfs(idx):
            if idx>=n:
                return [0]
            vals = dfs(idx+1)
            ret = []
            curr = nums[idx]
            for i in vals:
                ret.append(i+curr)
                ret.append(i-curr)
            return ret
        ans = 0
        ret = dfs(0)
        for val in ret:
            if val == target:
                ans+=1
        return ans
                