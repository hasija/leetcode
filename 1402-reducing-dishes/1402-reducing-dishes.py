class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        arr = sorted(satisfaction)
        n = len(arr)
        # [-9,-8,0,5]
        # max(-9*1+def, 9*0)
        max_d = {}

        # @lru_cache()
        def dp(ind, multi):
            if (ind,multi) in max_d:
                return max_d[(ind,multi)]
            if ind>=n:
                return 0
            val = arr[ind]
            out = max(val*multi+dp(ind+1, multi+1), dp(ind+1, multi))
            max_d[(ind, multi)]=out
            return out
        return dp(0,1)
                
        