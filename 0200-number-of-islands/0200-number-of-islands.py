class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        connected = {}
        self.ans = 0
        self.visited = set()
        
        def dfs(row, col):
            if grid[row][col]=='1':
                grid[row][col]='0'
                if 0<=row+1<rows:
                    dfs(row+1, col)
                if 0<=row-1<rows:
                    dfs(row-1, col)
                if 0<=col+1<cols:
                    dfs(row, col+1)
                if 0<=col-1<cols:
                    dfs(row, col-1)
                        

        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if cell == '1':
                    self.ans+=1
                    dfs(row, col)
        return self.ans
        
      