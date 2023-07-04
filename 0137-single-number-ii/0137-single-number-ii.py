class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        ones = 0
        tows = 0
        
        for i in nums:
            ones = (i^ones)&(~tows)
            tows = (i^tows)&(~ones)
        return ones