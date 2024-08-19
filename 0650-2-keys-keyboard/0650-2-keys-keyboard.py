class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def dp(curr, copied):
            if curr>n:
                return float('inf')
            if curr==n:
                return 0
            
            if (curr, copied) in memo:
                return memo[(curr, copied)]
            
            paste = dp(curr+copied,copied)+1
            copy_and_paste = dp(curr+curr, curr)+2
            memo[(curr, copied)] = min(paste, copy_and_paste)
            return memo[(curr, copied)]
        
        if n ==1:
            return 0
        return dp(1,1)+1