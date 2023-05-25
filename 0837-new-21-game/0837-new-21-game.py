class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float: 
        memo = [0]*(n+1)
        memo[0]=1
        out = 0
        if k ==0:
            return 1
            
        w = 1/maxPts
        for i in range(1, n+1):
            memo[i]=w
            
            if i<k:
                w+=w*1/maxPts
            else:
                out+=w
            if i>=maxPts:
                if i<maxPts+k-1:
                    w-=memo[i-maxPts]*1/maxPts
                else:
                    w = 0
        return out