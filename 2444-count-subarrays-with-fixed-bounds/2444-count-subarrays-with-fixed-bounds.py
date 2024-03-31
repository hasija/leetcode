class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_v = -1
        max_v = -1
        bad_v = -1

        for ind, i in enumerate(nums):
            if not minK<=i<=maxK:
                bad_v = ind
            if minK==i:
                min_v = ind
            if maxK == i:
                max_v = ind
            ans += max(0,min(min_v, max_v)-bad_v)
        return ans