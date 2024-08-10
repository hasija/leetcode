class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def build_arr(grid):
            rows = len(grid)*3
            cols = len(grid[0])*3
            arr = [[0]*cols for i in range(rows)]
            
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    curr_r=r*3
                    curr_c=c*3
                    curr = grid[r][c]
                    if curr==' ':
                        continue
                    elif curr == '/':
                        arr[curr_r][curr_c+2]=1
                        arr[curr_r+1][curr_c+1]=1
                        arr[curr_r+2][curr_c]=1
                    else:
                        arr[curr_r][curr_c]=1
                        arr[curr_r+1][curr_c+1]=1
                        arr[curr_r+2][curr_c+2]=1
            return arr
        arr = build_arr(grid)
        
        cnt = 0
        rows = len(arr)
        cols = len(arr[0])
        visited = set()
        
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for r,c in [[0,1],[1,0],[-1,0],[0,-1]]:
                new_r = i+r
                new_c = j+c
                if 0<=new_r<rows and 0<=new_c<cols and arr[new_r][new_c]!=1:
                    dfs(new_r, new_c)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and arr[i][j]!=1:
                    cnt+=1
                    dfs(i,j)
        
        return cnt