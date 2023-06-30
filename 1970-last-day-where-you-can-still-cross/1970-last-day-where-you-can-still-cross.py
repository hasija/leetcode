class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        day_visited = [0]*len(cells)
        l_day = 0
        r_day = len(cells)-1
        last_find = -1
        while l_day<=r_day:
            mid = (l_day+r_day)//2
            # print("this is lrmid", l_day,r_day, mid)
            grid = [[0]*col for i in range(row)]
            for r,c in cells[:mid+1]:
                grid[r-1][c-1]=1
            flag=False
            # print (grid)
            queue = [(0,i) for i in range(col) if grid[0][i]==0]
            # print ("start queue", queue)
            while queue:
                new_gen = []
                for old_r,old_c in queue:
                    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                        r= i+old_r
                        c= j +old_c
                        if 0<=r<row and 0<=c<col:
                            pass
                        else:
                            continue
                        if grid[r][c]!=0:
                            continue
                        elif r==row-1:
                            flag = True
                            break
                        else:
                            new_gen.append((r,c))
                            grid[r][c]=-1
                queue = new_gen
                if flag:
                    break
            # print ("FLAG", flag, "final lr",(mid+1,r_day) if flag else (l_day,mid-1))
            
            if flag:
                l_day=mid+1
                last_find = mid
                # print ("last find changed", last_find)
            else:
                r_day=mid-1
        return last_find+1
            
            
            
        