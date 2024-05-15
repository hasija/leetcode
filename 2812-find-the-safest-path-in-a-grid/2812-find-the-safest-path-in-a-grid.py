class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        thief = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    grid[r][c] = -1
                    thief.append((r,c))
        
        visited = set()
        nodes = thief.copy()
        dist = 1
        while nodes:
            new_nodes = []
            for r,c in nodes:
                for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_r = r+i
                    new_c = c+j
                    if 0<=new_r<ROW and 0<=new_c<COL and (new_r,new_c) not in visited and grid[new_r][new_c]!=-1:
                        grid[new_r][new_c]=dist
                        new_nodes.append((new_r,new_c))
                        visited.add((new_r, new_c))
            dist+=1
            nodes = new_nodes
        
        values = [i for i in range(1, dist)]
        # print (grid)
        
        
        def bfs(safe):
            # print ("check for safe", safe)
            arr = [(0,0)]
            target = (ROW-1, COL-1)
            visited = set()
            while arr:
                # print ("CHECKIN arr", arr, "visted", visited)
                new_arr = []
                for r,c in arr:
                    if 0<=r<ROW and 0<=c<COL and grid[r][c] !=-1 and (r,c) not in visited and grid[r][c]>=safe:
                        visited.add((r,c))
                        if (r,c)==target:
                            return True
                        [new_arr.append((i+r, j+c)) for i,j in [(1,0), (-1,0), (0,1), (0,-1)] ]
                arr = new_arr
                
            
        
        
        
        
        
        
        # print ("VALUES", values)
        l = 0 
        r = len(values)-1
        while l<=r:
            # print ("start",l,r)
            mid = (l+r)//2
            safe = values[mid]
            if bfs(safe):
                l=mid+1
            else:
                r = mid-1
            # print ("end", l, r)
        if r>=0:
            return values[r]
        return 0
        