class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] !=0:
            return -1
        arr = [(0,0)]
        visited = set()
        final_r = len(grid)-1
        final_c = len(grid[0])-1
        count = 0
        if final_r == final_c ==0:
            return 1
        def get_8_direction(r,c):
            new_set = set()
            if 0 <=r-1<=final_r:
                if grid[r-1][c]==0:
                    new_set.add((r-1,c))
                if 0 <=c+1<=final_c and grid[r-1][c+1]==0:
                    new_set.add((r-1,c+1))
                if 0 <=c-1<=final_c and grid[r-1][c-1]==0:
                    new_set.add((r-1,c-1))
            if 0 <=r+1<=final_r:
                if grid[r+1][c]==0:
                    new_set.add((r+1,c))
                if 0 <=c+1<=final_c and grid[r+1][c+1]==0:
                    new_set.add((r+1,c+1))
                if 0 <=c-1<=final_c and grid[r+1][c-1]==0:
                    new_set.add((r+1,c-1))
            if 0 <=c+1<=final_c and grid[r][c+1]==0:
                new_set.add((r,c+1))
            if 0 <=c-1<=final_c and grid[r][c-1]==0: 
                new_set.add((r,c-1))
            return new_set
        
        while len(arr)!=0:
            next_traversal = set()
            count+=1
            for r,c in arr:
                if (r,c) in visited:
                    continue
                else:
                    visited.add((r,c))
                to_visit = get_8_direction(r,c)
                # print ('nre visits',to_visit)
                if (final_r,final_c) in to_visit:
                    return count+1
                next_traversal = next_traversal.union(to_visit)
            # print (next_traversal)
            arr = next_traversal
        
        return -1