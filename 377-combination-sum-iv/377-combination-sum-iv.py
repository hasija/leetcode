class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=True)
        self.sum = {}
        self.out = 0
        def dfs(curr_sum):
            if curr_sum in self.sum:
                return self.sum[curr_sum]
            if curr_sum == target:
                return 1
            if curr_sum>target:
                return 0
            if curr_sum<target:
                tmp = 0
                for val in nums:
                    tmp+=dfs(curr_sum+val)
                self.sum[curr_sum]=tmp
                self.out+=tmp
                return tmp
        total = 0
        for val in nums:
            out = dfs(val)
            total+=out
            if val not in self.sum and val<=target:
                self.sum[val]=out
            
        # print (self.sum)
        return total

        