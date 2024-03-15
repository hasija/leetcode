class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cal_pre_post = 1
        ans = [1]*len(nums)
        for ind in range(1, len(nums)):
            cal_pre_post *= nums[ind-1]
            ans[ind] = cal_pre_post
        
        cal_pre_post = 1
        for ind in range(len(nums)-2, -1, -1):
            cal_pre_post *= nums[ind+1]
            ans[ind] *= cal_pre_post
        return ans