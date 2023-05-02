class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for i in nums:
            val*=i
        if val>0:
            return 1
        elif val<0:
            return -1
        return 0