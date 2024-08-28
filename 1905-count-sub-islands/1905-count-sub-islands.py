class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        ROWS = len(grid2)
        COLS = len(grid2[0])
        visited = set()
        
        def get_island(r,c):
            all_maps = []
            if grid2[r][c] and (r,c) not in visited:
                visited.add((r,c))
                all_maps = [(r,c)]
                for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                    new_r = r+i
                    new_c = c+j
                    if 0<=new_r<ROWS and 0<=new_c<COLS:
                        all_maps+=get_island(new_r,new_c)
            return all_maps

        
        
        def cross_check(all_map):
            for r,c in all_map:
                if not grid1[r][c]:
                    return False
            return True
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid2[r][c]:
                    all_map = get_island(r,c)
                    if cross_check(all_map):
                        ans+=1
        return ans
            