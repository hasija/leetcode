class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        LEN = len(nums)
        self.ans = 0
        def dfs(ind, past):
            if past is None:
                self.ans+=nums[ind]
                curr = nums[ind]
            else:
                self.ans+=nums[ind]^past
                curr = nums[ind]^past
            
            for i in range(ind+1, LEN):
                dfs(i, curr)
        for i in range(LEN):
            dfs(i, None)
        return self.ans

                
            