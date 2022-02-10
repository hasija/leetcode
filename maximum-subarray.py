class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        old_val=None
        max_val = -float('inf')
        for idx in nums:
            if old_val is None:
                old_val = idx
            else:
                if idx + old_val> idx:
                    old_val=idx+old_val
                else:
                    old_val = idx
            if old_val>max_val:
                max_val=old_val
        return max_val
