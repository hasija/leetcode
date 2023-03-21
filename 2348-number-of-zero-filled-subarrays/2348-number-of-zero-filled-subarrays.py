class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        prev = 0
        total = 0
        for val in nums:
            if val==0:
                total+=1
                total+=prev
                prev+=1
            if val!=0:
                prev = 0
        return total
        