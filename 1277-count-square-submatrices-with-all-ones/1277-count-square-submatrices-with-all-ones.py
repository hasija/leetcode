class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def dp(i,j):
            if not(i<ROWS and j<COLS):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if matrix[i][j]!=1:
                return 0
            
            ans = 1
            right = dp(i+1, j)
            bot = dp(i, j+1)
            diag = dp(i+1, j+1)
            ans += min(right, bot, diag)
            memo[(i,j)] = ans
            return ans
        
        out = 0
        for i in range(ROWS):
            for j in range(COLS):
                out+= dp(i,j)
        return out