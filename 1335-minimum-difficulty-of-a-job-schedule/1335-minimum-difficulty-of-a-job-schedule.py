class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)
        if d>n:
            return -1
        
        @lru_cache(None)
        def dfs(start, d):
            if d==1:
                return max(jobDifficulty[start:])
            res, maxD = float('inf'), 0
            
            for i in range(start, n-d+1):
                maxD = max(maxD, jobDifficulty[i])
                res = min(res, maxD+dfs(i+1, d-1))
            return res
        return dfs(0, d)
            
        