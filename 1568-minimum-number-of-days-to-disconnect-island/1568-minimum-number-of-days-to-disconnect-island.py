class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.cycle = False
        
        
        def count_lands():
            self.visited = set()
            cnt = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c]==1 and (r,c) not in self.visited:
                        dfs(r,c)
                        cnt+=1
            return cnt
        
        def dfs(r,c):
            if (r,c) in self.visited:
                return
            self.visited.add((r,c))
            for i,j in [[0,1],[1,0],[-1,0],[0,-1]]:
                row = r+i
                col = c+j
                if 0<=row<rows and 0<=col<cols and grid[row][col]==1:
                    dfs(row,col)
        ans = 0
        
        base = count_lands()
        if base==0 or base>1:
            return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    grid[r][c]=0
                    cnt = count_lands()
                    if cnt>1 or cnt==0:
                        return 1
                    grid[r][c]=1
      
        return 2