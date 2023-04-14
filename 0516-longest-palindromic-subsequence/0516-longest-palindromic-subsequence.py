class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        i = 0
        j = len(s)-1
        memo = {}
        
        def dfs(i,j):
            if ((i,j) in memo):
                return memo[(i,j)]
            if i==j:
                return 1
            if i>=len(s) or j<0 or i>j:
                return 0
            if s[i]==s[j]:
                out = 2+dfs(i+1, j-1)
                memo[(i,j)] = out
                return out
            else:
                out =  max(dfs(i+1, j),  dfs(i, j-1))
                memo[(i,j)] = out
                return out
        return dfs(i, j)