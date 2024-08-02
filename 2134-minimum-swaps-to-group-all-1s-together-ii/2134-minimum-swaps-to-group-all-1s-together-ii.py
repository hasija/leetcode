class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = sum(nums)
        n = len(nums)
        cnt = mx = sum(nums[:window])
        for i in range(window, 2*n):
            if i>=n+window:
                break
            cnt += nums[i%n]
            cnt -=nums[(i-window)%n]
            mx = max(cnt, mx)
        return window-mx