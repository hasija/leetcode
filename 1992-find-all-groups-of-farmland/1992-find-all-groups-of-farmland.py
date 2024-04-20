class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        rows = len(land)
        cols = len(land[0])
        def dfs(r,c):
            cell = land[r][c]
            if cell == 1:
                land[r][c] = 0
                mr1 = mr2 = mc1 = mc2 = -1
                if r+1<rows:
                    mr1,mc1 = dfs(r+1,c)
                if c+1<cols:
                    mr2, mc2 = dfs(r, c+1)
                return max(mr1, mr2, r), max(mc1, mc2, c)
            else:
                return -1,-1
        
        for row in range(rows):
            for col in range(cols):
                cell = land[row][col]
                if cell == 1:
                    first = [row, col]
                    second = list(dfs(row, col))
                    # print (first+second)
                    ans.append(first+second)
        return ans