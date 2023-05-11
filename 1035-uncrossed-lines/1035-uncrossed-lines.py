class Solution:
    def maxUncrossedLines(self, n: List[int], m: List[int]) -> int:
        
        cache = {}
        
        def dp(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            out = 0
            if i>=len(n) or j>=len(m):
                return 0
            if n[i]==m[j]:
                out = 1+dp(i+1, j+1)
            out2 = dp(i, j+1)
            out3 = dp(i+1, j)
            out = max(out, out2, out3)
            cache[(i,j)]=out
            # print ("return ",i,j,out)
            return out
        return dp(0,0)
            
        