class Solution:
    def maxValueOfCoins(self, piles, K):
        total = len(piles)
        dp = [[-1]*(K+1) for i in range(total+1)]
        
        
        def dfs(i , k):
            if dp[i][k]!=-1:
                return dp[i][k]
            if i>=total:
                return 0
            
            local_max = dfs(i+1,k)
            curr = 0
            # local_max = 0
            for local_k in range(min(k,len(piles[i]))):
                curr += piles[i][local_k]
                out = dfs(i+1, k-local_k-1)
                curr_max = out+curr
                local_max = max(local_max, curr_max)
            dp[i][k]=local_max
            return local_max
        return dfs(0,K)
        
            