class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        all_keys = [0]*6
        m = len(grid)
        n = len(grid[0])
        start_i, start_j = 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    all_keys[ord(grid[i][j])-ord('a')]=1
                elif grid[i][j]=='@':
                    start_i = i
                    start_j = j
        
        moves = 0
        state = [0]*6
        curr_level = [(start_i, start_j, state)]
        visited = set((start_i, start_j, tuple(state)))
        while curr_level:
            new_level = []
            for row, col, states in curr_level:
                # print ("CURR ROW COL", row, col)
                for r,c in ([0,1],[0,-1],[1,0],[-1,0]):
                    new_state = states.copy()
                    new_r, new_c = row+r, col+c
                    
                    if 0<=new_r<m and 0<=new_c<n:
                        pass
                    else:
                        continue
                        
                    if grid[new_r][new_c]=='#':
                        continue
                    
                    if grid[new_r][new_c] in ".@":
                        if (new_r,new_c, tuple(new_state)) not in visited:
                            new_level.append((new_r,new_c, new_state))
                            visited.add((new_r,new_c, tuple(new_state)))
                    
                    elif grid[new_r][new_c].islower():
                        idx = ord(grid[new_r][new_c])-ord('a')
                        new_state[idx]=1
                        # print (new_state, all_keys)
                        if new_state == all_keys:
                            return moves+1
                        if (new_r, new_c, tuple(new_state)) not in visited:
                            new_level.append((new_r, new_c, new_state))
                            visited.add((new_r, new_c, tuple(new_state)))
                    else:
                        idx = ord(grid[new_r][new_c].lower())-ord('a')
                        if new_state[idx] and (new_r, new_c, tuple(new_state)) not in visited:
                            new_level.append((new_r, new_c, new_state))
                            visited.add((new_r, new_c, tuple(new_state)))
                    
            moves+=1
            curr_level=new_level
        return -1
                            
                            
        
        
        