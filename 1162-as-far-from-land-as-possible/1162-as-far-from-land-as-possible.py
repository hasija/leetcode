class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = grid.copy()
        move = []
        distance = -1
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                curr = grid[i][j]
                if curr == 1:
                    move.append((i,j))
        # print ("MOVES OF 1s", move)
        # Collected all the 1s
        
        if len(move)==0 or len(move)==rows*cols:
            return -1
        
        # Check func
        
        def check_direct(i,j):
            if i<0 or j<0 or j>=cols or i>rows:
                return False
            try:
                upper = visited[i][j]
                if upper == 0:
                    visited[i][j]=1
                    return True
                return False
            except:
                pass
            return False
        
        
        while move:
            new_move = []
            for i,j in move:
                
                # Check 4 directions
                
                if check_direct(i+1,j):
                    new_move.append((i+1,j))
                
                if check_direct(i-1,j):
                    new_move.append((i-1,j))
                
                if check_direct(i,j+1):
                    new_move.append((i,j+1))
                
                if check_direct(i,j-1):
                    new_move.append((i,j-1))
            # print ("AFTER ITERATION", visited, 'Os converted',new_move)
            move = new_move.copy()
            distance+=1
            
        return distance
                
                    
                
        
        