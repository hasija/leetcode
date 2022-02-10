class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = []
        count = 0
        # def check_connected(x,y):
        #     # print (f"cordinates: {x,y}")
        #     # print (island)
        #     for land in island:
        #         if x>=1 and grid[x-1][y]=="1" and (x-1,y) in land:
        #             # print("1")
        #             land.add((x,y))
        #             return
        #         if y>0 and grid[x][y-1]=="1" and (x,y-1) in land:
        #             # print ("2")
        #             land.add((x,y))
        #             return
        #     # print ("3")
        #     tmp_set = set()
        #     tmp_set.add((x,y))
        #     island.append(tmp_set)
        def dfs(x,y):
            if x<0 or y<0 or y>=len(grid[0]) or x>=len(grid) or grid[x][y]!="1":
                return
            grid[x][y]="#"
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=="1":
                    dfs(x,y)
                    count+=1
        # print (len(island))
        return count