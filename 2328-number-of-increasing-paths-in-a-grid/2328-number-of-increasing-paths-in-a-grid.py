class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        r = len(grid)
        mod = (10**9)+7
        c = len(grid[0]) 
        dp = [[1]*c for i in range(r)]
        
        cells = [[i,j] for i in range(r) for j in range(c) ]
        
        cells = sorted(cells, key=lambda x: grid[x[0]][x[1]])

        
        def get_path(x,y,i,j):
            if 0<=x<r and 0<=y<c and grid[i][j]<grid[x][y]:
                dp[x][y]+=dp[i][j]
                dp[x][y] = dp[x][y]%mod
        for i, j in cells:
            get_path(i-1,j,i,j)
            get_path(i+1,j,i,j)
            get_path(i,j-1,i,j)
            get_path(i,j+1,i,j)
        # print (dp)
        return sum(sum(r)%mod for r in dp)%mod