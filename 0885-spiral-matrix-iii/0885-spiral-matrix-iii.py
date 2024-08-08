class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows*cols
        visited = set()

        steps = 1
        move = 'right'
        r=rStart
        c=cStart
        visited = [[r,c]]
        while len(visited)!=total:
            for i in range(steps):
                if move=='right':
                    c+=1
                elif move=='down':
                    r+=1
                elif move=='left':
                    c-=1
                elif move=='up':
                    r-=1
                # print (r,c)
                if 0<=r<rows and 0<=c<cols:
                    # print ("moved inside?")
                    visited.append([r,c])
            if move=='right':
                move='down'
            elif move=='down':
                move='left'
                steps+=1
            elif move=='left':
                move='up'
            elif move=='up':
                move='right'
                steps+=1
        return visited
                
            