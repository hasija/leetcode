class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        
        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            ans = float('inf')
            for j in range(1, i+1):
                sqr_j = sqrt(j)
                if sqr_j != int(sqr_j):
                    continue
                ans = min(ans, dp(i%j)+i//j)
            memo[i] = ans
            return memo[i]
        return dp(n)
            
                
                    
            
                    
                