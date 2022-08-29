class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def dfs(i,j):
            if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]):
                if grid[i][j]=="1":
                    grid[i][j]="-1"
                    dfs(i+1,j)
                    dfs(i-1,j)
                    dfs(i,j+1)
                    dfs(i,j-1)
                    return 1
            else:
                return -1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(row, col)==1:
                    count+=1
        # print (grid)
        # print (count)
        return count