class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = -float('inf')
        for i in range(ROWS):
            for j in range(COLS):
                c1 = grid[i-1][j] if i>0 else float('inf')
                c2 = grid[i][j-1] if j>0 else float('inf')
                min_till_now = min(c1,c2)
                ans = max(grid[i][j]-min_till_now, ans)
                # updating min val in place
                grid[i][j] = min(min_till_now,grid[i][j])
        return ans