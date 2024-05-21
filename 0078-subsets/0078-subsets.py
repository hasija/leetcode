class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        def dfs(ind, past):
            if ind>=len(nums):
                return
            past.append(nums[ind])
            self.ans.append(past.copy())
            for i in range(ind+1, len(nums)):
                dfs(i, past.copy())
        for i in range(len(nums)):
            dfs(i, [])
        return self.ans