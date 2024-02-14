class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        posi = 0
        neg = 1
        
        for i in nums:
            if i>0:
                ans[posi] = i
                posi+=2
            else:
                ans[neg] = i
                neg+=2
        return ans