class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}
        cols = len(grid[0])
        rows = len(grid)
        def dp(r1,r2):
            if (r1, r2) in memo:
                return memo[(r1,r2)]
            
            if r1[0]>=rows:
                return 0
            if r1[1]>=cols or r1[1]<0 or r2[1]<0 or r2[1]>=cols:
                return 0
            out = 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    out = max(dp((r1[0]+1,r1[1]+i), ((r2[0]+1,r2[1]+j))), out)
                    
            
            out += grid[r1[0]][r1[1]]+grid[r2[0]][r2[1]]
            if r1==r2:
                out -= grid[r1[0]][r1[1]]
            # print ("out",out,'r1', r1, 'r2', r2)
            memo[(r1, r2)] = out
            return out
        return dp((0,0),(0,cols-1))
    
    
    