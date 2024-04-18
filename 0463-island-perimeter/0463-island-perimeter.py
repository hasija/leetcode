class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for ind, row in enumerate(grid):
            for col, cell in enumerate(row):
                if ind == 0 or grid[ind-1][col]==0:
                    top = 1
                else:
                    top = 0
                if ind == len(grid)-1 or grid[ind+1][col]==0:
                    bot = 1
                else:
                    bot = 0
                if col == 0 or grid[ind][col-1]==0:
                    left = 1
                else:
                    left = 0
                if col == len(grid[0])-1 or grid[ind][col+1]==0:
                    right = 1
                else:
                    right = 0
                if cell == 1:
                    ans+=top+bot+right+left
        return ans
                    