import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        change=True
        max_val = nums[0]
        prefix = nums[0]
        for i in range(1, n):
            curr = nums[i]
            prefix += curr
            if curr<max_val:
                continue
            max_val = max(max_val, math.ceil(prefix/(i+1)))
        return max_val
            