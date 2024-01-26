class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        MOD = (10**9)+7
        def dp(moves, r, c):
            if r>=m or c>=n or r<0 or c<0:
                return 1
            if moves<=0:
                return  0
            if (moves,r,c) in memo:
                return memo[(moves,r,c)]
            total = 0
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r = r+i
                new_c = c+j
                total+=dp(moves-1, new_r, new_c)
            memo[(moves, r,c)] = total%MOD
            return memo[(moves,r,c)]
        return dp (maxMove, startRow, startColumn)%MOD