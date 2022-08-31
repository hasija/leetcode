class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)-1
        n=len(heights[0])-1
        # print("mn",m,n)
        def cell_border(r, c):
            a=False
            b=False
            if r==m:
                b=True
            if r==0:
                a=True
            if c==0:
                a=True
            if c==n:
                b=True
            return a, b
        
        def dfs(r, c, h, visited):
            visited.add((r,c))
            if r<=m and r>=0 and c<=n and c>=0:
                new_h = heights[r][c]
                if heights[r][c]<=h:
                    if (r,c) in new_dict:
                        return new_dict[(r,c)]
                    a ,b =cell_border(r, c)
                    a1=b1=a2=b2=a3=b3=a4=b4=False
                        
                    if not a or not b:
                        if (r+1,c) not in visited:
                            a1, b1 = dfs(r+1, c, new_h, visited.copy())
                            if (a or a1) and (b or b1):
                                return True, True
                        if (r-1,c) not in visited:
                            a2, b2 = dfs(r-1, c, new_h, visited.copy())
                            if (a or a2) and (b or b2):
                                return True, True
                        if (r,c+1) not in visited:
                            a3, b3 = dfs(r, c+1, new_h, visited.copy())
                            if (a or a3) and (b or b3):
                                return True, True
                        if (r,c-1) not in visited:
                            a4, b4 = dfs(r, c-1, new_h, visited.copy())
                            if (a or a4) and (b or b4):
                                return True, True
                        if a or a1 or a2 or a3 or a4:
                            a= True
                        if b or b1 or b2 or b3 or b4:
                            b= True
                    return a,b
               
                else:
                    return False, False
            else:
                return False, False
                
        out = []
        new_dict = {}
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                a,b = dfs(row, col, float('inf'), set())
                new_dict[(row,col)]=(a,b)
                if a and b:
                    out.append([row, col])
        return out