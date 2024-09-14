class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ = max(nums)
        cnt=0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == max_:
                cnt+=1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
                