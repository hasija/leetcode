class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(idx):
            if idx>=n:
                return Counter()
            cnt = dfs(idx+1)
            curr = nums[idx]
            new_cnt = Counter()
            for k in cnt:
                new_cnt[k+curr] +=cnt[k]
                new_cnt[k-curr] +=cnt[k]

            cnt = new_cnt
            if len(cnt) == 0:
                cnt[curr]+=1
                cnt[-curr]+=1            
            return cnt
        cnt = dfs(0)
        # print(cnt)
        return cnt[target]
                