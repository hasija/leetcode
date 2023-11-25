class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        pre_s = 0
        suff_s = sum(nums)
        n = len(nums)
        res = []
        
        for ind, i in enumerate(nums):
            cnt = ind
            suff_s -= i
            ans = (cnt*i)-(pre_s)+suff_s-((n-1-cnt)*i)
            res.append(ans)
            pre_s+=i
        return res