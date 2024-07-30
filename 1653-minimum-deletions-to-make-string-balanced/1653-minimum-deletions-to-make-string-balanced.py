class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        memo = [[-1]*2 for i in range(n)]
        def dfs(idx, flag):
            if idx>=n:
                return 0
            if memo[idx][flag]!=-1:
                return memo[idx][flag]
            curr = s[idx]
            if flag and curr=='a':
                out = dfs(idx+1, flag)+1
            elif not flag and curr=='a':
                out = dfs(idx+1, flag)
            elif not flag and curr=='b':
                out = min(dfs(idx+1, 0)+1, dfs(idx+1, 1))
            else:
                out = dfs(idx+1, flag)
            memo[idx][flag]=out
            return out
        return dfs(0, 0) 
            
                
                