class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        ttl = sum(nums)
        hmap = {0:-1}
        curr = 0
        needed = ttl%p
        if needed == 0:
            return 0
        ans = n
        for idx, i in enumerate(nums):
            curr+=i
            curr%=p
            tmp_need = (curr+p-needed)%p
            if tmp_need in hmap:
                ans = min(ans, idx-hmap[tmp_need])
            hmap[curr]=idx
        return -1 if ans==n else ans
        