class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def recurse(i,j, visited):
            # print ("inside loop",i,j,visited)
            if not(0<=i<len(grid) and 0<=j<len(grid[0])):
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            local_max = 0
            if grid[i][j]==0:
                return 0
            for new_i, new_j in [(1,0), (-1,0), (0,1), (0,-1)]:
                local_max = max(local_max, recurse(new_i+i, new_j+j, set(visited)))
            return local_max+grid[i][j]
        
        MAX = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                MAX=max(recurse(i,j, set()), MAX)
                # print ("local max", MAX, i, j)
                # break
            # break
        return MAX

            