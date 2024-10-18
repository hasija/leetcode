class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(idx):
            if idx==n:
                return [0]
            arr = dp(idx+1)
            curr = nums[idx]
            new_arr = []
            for i in arr:
                tmp = i|curr
                new_arr.append(tmp)
            new_arr = new_arr+arr
            return new_arr
        
        all_arr = dp(0)
        max_or = 0
        for i in nums:
            max_or|=i
        ans = 0
        for i in all_arr:
            if i ==max_or:
                ans+=1
        return ans