class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        first_move =  True if grid[0][1]<=1 or grid[1][0]<=1 else False
        if not first_move:
            return -1
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = [(0,(0,0))]
        heapq.heapify(queue)
        visited = set()
        visited.add((0,0))
        while queue:
            curr_time, curr_posi = heapq.heappop(queue)
            # print(curr_time, curr_posi)
            for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                r = i+curr_posi[0]
                c = j+curr_posi[1]
                if 0<=r<ROWS and 0<=c<COLS and (r,c) not in visited:
                    
                    buffer_sec = 1 if (grid[r][c]-curr_time)%2==0 else 0
                    new_time = max(curr_time+1, grid[r][c]+buffer_sec)
                    if (r,c)==(ROWS-1, COLS-1):
                        return new_time
                    else:
                        visited.add((r,c))
                        # print("adding next",(new_time, (r,c)) )
                        heapq.heappush(queue, (new_time, (r,c)))
        
                        
            