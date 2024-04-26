class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        cols = len(grid[0])
        def dp(i, last):
            if i>=len(grid):
                return 0
            if (i, last) in memo:
                return memo[(i, last)]
            min_val = float('inf')
            min_c = None
            for ind in range(cols):
                if ind==last:
                    continue
                ans = dp(i+1, ind)+grid[i][ind]
                if ans<min_val:
                    min_val = ans
                #     min_c = [ind]
                # elif ans == min_val:
                #     min_c.append(ind)
            memo[(i, last)] =  min_val
            return memo[(i, last)]
        return dp(0, None)
                