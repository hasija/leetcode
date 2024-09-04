class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        posi = [0,0]
        moves = ['up','right','down','left']
        direction = 0
        obstacles = set(map(tuple,obstacles))
        ans = 0
        def check_obstacle(steps, direction):

            old = posi.copy()
            for i in range(steps):
                if moves[direction]=='up':
                    new_posi = [old[0],old[1]+1]
                elif moves[direction]=='down':
                    new_posi = [old[0],old[1]-1]
                elif moves[direction]=='left':
                    new_posi = [old[0]-1,old[1]]
                else:
                    new_posi = [old[0]+1,old[1]]
                if tuple(new_posi) in obstacles:
                    return old
                else:
                    old = new_posi
            return old
        
        for command in commands:
            if command == -1:
                direction+=1
                direction%=4
                continue
            elif command ==-2:
                direction-=1
                if direction==-1:
                    direction = 3
                continue
            posi = check_obstacle(command, direction)
            ans = max(posi[0]**2 + posi[1]**2, ans)
        return ans
            
          
            