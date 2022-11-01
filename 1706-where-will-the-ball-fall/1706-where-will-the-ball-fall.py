class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        col = len(grid[0])
        row = len(grid)
        @lru_cache()
        def dfs(r,c):
            if r == row:
                return c
            curr =  grid[r][c]
            if curr == 1:
                # moving to right
                if c+1>=col:
                    return -1
                elif grid[r][c+1]==-1:
                    return -1
                else:
                    return dfs(r+1,c+1)
            elif curr ==-1:
                # Moving left
                if c-1<0:
                    return -1
                elif grid[r][c-1]==1:
                    return -1
                else:
                    return dfs(r+1, c-1)
        out = []
        for i in range(col):
            out.append(dfs(0, i))
        return out
                
                    